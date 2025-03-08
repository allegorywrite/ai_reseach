# SE(3)上のCCBFを用いた最適化

本ドキュメントでは、リー群およびSE(3)上でのConsensus-Based Control Barrier Function (CCBF)を用いた最適化問題の定式化と解法について詳細に説明します。特に、ドローンのダイナミクスをSE(3)上で表現し、CCBFを用いた安全制約付きMPC問題を解く方法に焦点を当てます。

## 1. リー群とSE(3)の基礎

### 1.1 リー群の定義と性質

リー群は、滑らかな多様体であり、かつ群構造を持つ数学的対象です。形式的には、リー群 $G$ は以下の性質を持つ多様体です：

- $G$ は滑らかな多様体である
- 群演算 $\cdot: G \times G \rightarrow G$ は滑らかである
- 逆元を取る操作 $^{-1}: G \rightarrow G$ は滑らかである

リー群に対応するリー代数 $\mathfrak{g}$ は、$G$ の単位元における接空間であり、ベクトル空間構造とリー括弧積 $[\cdot, \cdot]: \mathfrak{g} \times \mathfrak{g} \rightarrow \mathfrak{g}$ を持ちます。

リー群とリー代数の間には、指数写像 $\exp: \mathfrak{g} \rightarrow G$ と対数写像 $\log: G \rightarrow \mathfrak{g}$ が定義され、これらによってリー代数の元（ベクトル）とリー群の元（行列など）を相互に変換できます。

### 1.2 SE(3)の定義と表現

特殊ユークリッド群 SE(3) は、3次元空間における剛体の位置と姿勢（合わせてポーズと呼ぶ）を表現するリー群です。SE(3) の元は、回転行列 $R \in SO(3)$ と並進ベクトル $p \in \mathbb{R}^3$ の組 $(R, p)$ として表現できます。行列形式では：

$$X = \begin{bmatrix} R & p \\ 0_{1 \times 3} & 1 \end{bmatrix} \in SE(3)$$

ここで、$R \in SO(3)$ は $R^T R = I$ かつ $\det(R) = 1$ を満たす $3 \times 3$ の回転行列、$p \in \mathbb{R}^3$ は並進ベクトルです。

SE(3) に対応するリー代数 $\mathfrak{se}(3)$ の元は、$\mathbb{R}^6$ のベクトル $\xi = [\omega^T, v^T]^T$ として表現できます。ここで、$\omega \in \mathbb{R}^3$ は角速度ベクトル、$v \in \mathbb{R}^3$ は線速度ベクトルです。$\mathfrak{se}(3)$ の元を行列形式で表現すると：

$$\xi^\wedge = \begin{bmatrix} \omega^\wedge & v \\ 0_{1 \times 3} & 0 \end{bmatrix} \in \mathfrak{se}(3)$$

ここで、$\omega^\wedge$ は $\omega$ の歪対称行列：

$$\omega^\wedge = \begin{bmatrix} 0 & -\omega_3 & \omega_2 \\ \omega_3 & 0 & -\omega_1 \\ -\omega_2 & \omega_1 & 0 \end{bmatrix}$$

指数写像 $\exp: \mathfrak{se}(3) \rightarrow SE(3)$ は以下のように定義されます：

$$\exp(\xi^\wedge) = \begin{bmatrix} \exp(\omega^\wedge) & J(\omega) v \\ 0_{1 \times 3} & 1 \end{bmatrix}$$

ここで、$\exp(\omega^\wedge)$ は $SO(3)$ 上の指数写像で、$J(\omega)$ はヤコビアン行列：

$$J(\omega) = \frac{\sin(\|\omega\|)}{\|\omega\|} I + \left(1 - \frac{\sin(\|\omega\|)}{\|\omega\|}\right) \frac{\omega \omega^T}{\|\omega\|^2} + \frac{1 - \cos(\|\omega\|)}{\|\omega\|} \omega^\wedge$$

対数写像 $\log: SE(3) \rightarrow \mathfrak{se}(3)$ は指数写像の逆操作です。

### 1.3 SE(3)上のドローンダイナミクス

ドローンのダイナミクスをSE(3)上で表現すると、状態は位置 $p \in \mathbb{R}^3$ と姿勢 $R \in SO(3)$ の組 $(R, p)$ となります。連続時間のダイナミクスは以下のように記述できます：

$$\dot{R} = R \omega^\wedge$$
$$\dot{p} = v$$
$$m \dot{v} = m g e_3 + R f$$
$$J \dot{\omega} = J \omega \times \omega + \tau$$

ここで：
- $m$ はドローンの質量
- $g$ は重力加速度
- $e_3 = [0, 0, 1]^T$ は鉛直上向きの単位ベクトル
- $f = [0, 0, f]^T$ は機体座標系におけるスラスト力（$z$軸方向）
- $J$ は慣性モーメント行列
- $\tau$ はトルク入力

SE(3)の元 $X = (R, p)$ とその時間微分 $\dot{X} = (R \omega^\wedge, v)$ を用いると、ダイナミクスは以下のようにコンパクトに表現できます：

$$\dot{X} = X \xi^\wedge$$
$$M \dot{\xi} = \text{ad}_\xi^* (M \xi) + F_g + F_u$$

ここで、$M$ は質量・慣性行列、$\text{ad}_\xi^*$ は随伴表現、$F_g$ は重力項、$F_u$ は制御入力です。

## 2. リー群上のControl Barrier Function (CBF)

### 2.1 リー群上のCBFの定義

リー群 $G$ 上のControl Barrier Function (CBF) は、安全集合 $\mathcal{C} = \{x \in G : h(x) \geq 0\}$ を定義する滑らかな関数 $h: G \rightarrow \mathbb{R}$ です。$h$ がCBFであるための条件は、すべての $x \in G$ に対して、ある拡張クラス $\mathcal{K}$ 関数 $\alpha$ が存在し、以下を満たす制御入力 $u$ が存在することです：

$$\mathcal{L}_f h(x) + \mathcal{L}_g h(x) u + \alpha(h(x)) \geq 0$$

ここで、$\mathcal{L}_f h$ と $\mathcal{L}_g h$ はそれぞれ $h$ の $f$ と $g$ に関するリー微分です。

リー群上でのリー微分は、リー代数を用いて定義されます。具体的には、$h: G \rightarrow \mathbb{R}$ のリー微分は以下のように計算されます：

$$\mathcal{L}_f h(x) = \frac{d}{dt} h(x(t))|_{t=0} = \langle \nabla h(x), f(x) \rangle_x$$

ここで、$\nabla h(x)$ は $h$ の勾配で、$\langle \cdot, \cdot \rangle_x$ はリー群 $G$ 上の点 $x$ における内積です。

### 2.2 SE(3)上のCBFの具体例

SE(3)上のCBFの具体例として、ドローンの安全飛行領域を定義するCBFを考えます。例えば、ドローンが特定の領域内に留まるための障害物回避CBFは以下のように定義できます：

$$h_{\text{obs}}(X) = \|p - p_{\text{obs}}\|^2 - r_{\text{safe}}^2$$

ここで、$p$ はドローンの位置、$p_{\text{obs}}$ は障害物の位置、$r_{\text{safe}}$ は安全距離です。$h_{\text{obs}}(X) \geq 0$ を満たす状態は、ドローンが障害物から安全距離以上離れていることを意味します。

また、ドローンのカメラが特定のターゲットを視野内に保つためのCBFは以下のように定義できます：

$$h_{\text{FOV}}(X) = \cos(\theta_{\text{max}}) - \frac{(p_{\text{target}} - p)^T R e_1}{\|p_{\text{target}} - p\|}$$

ここで、$\theta_{\text{max}}$ は視野角の半分、$e_1 = [1, 0, 0]^T$ はカメラの光軸方向の単位ベクトル（機体座標系）、$p_{\text{target}}$ はターゲットの位置です。$h_{\text{FOV}}(X) \geq 0$ を満たす状態は、ターゲットがカメラの視野内にあることを意味します。

### 2.3 SE(3)上のCBFの微分

SE(3)上のCBF $h(X)$ のリー微分を計算するには、$h$ の勾配 $\nabla h(X)$ を計算し、ダイナミクス $f(X)$ との内積を取ります。SE(3)上の点 $X = (R, p)$ における $h$ の勾配は、$\mathfrak{se}(3)$ の元として表現されます：

$$\nabla h(X) = \left[ \frac{\partial h}{\partial R}, \frac{\partial h}{\partial p} \right]$$

ここで、$\frac{\partial h}{\partial R}$ は $h$ の $R$ に関する勾配で、$\mathfrak{so}(3)$ の元として表現されます。$\frac{\partial h}{\partial p}$ は $h$ の $p$ に関する勾配で、$\mathbb{R}^3$ のベクトルです。

例えば、障害物回避CBF $h_{\text{obs}}(X) = \|p - p_{\text{obs}}\|^2 - r_{\text{safe}}^2$ の勾配は：

$$\frac{\partial h_{\text{obs}}}{\partial R} = 0$$
$$\frac{\partial h_{\text{obs}}}{\partial p} = 2(p - p_{\text{obs}})$$

視野内保持CBF $h_{\text{FOV}}(X) = \cos(\theta_{\text{max}}) - \frac{(p_{\text{target}} - p)^T R e_1}{\|p_{\text{target}} - p\|}$ の勾配は：

$$\frac{\partial h_{\text{FOV}}}{\partial R} = -\frac{(p_{\text{target}} - p) e_1^T}{\|p_{\text{target}} - p\|}$$
$$\frac{\partial h_{\text{FOV}}}{\partial p} = \frac{R e_1}{\|p_{\text{target}} - p\|} - \frac{(p_{\text{target}} - p)^T R e_1}{\|p_{\text{target}} - p\|^3} (p_{\text{target}} - p)$$

これらの勾配を用いて、CBFのリー微分を計算できます。

## 3. SE(3)上のConsensus-Based Control Barrier Function (CCBF)

### 3.1 CCBFの定義と性質

Consensus-Based Control Barrier Function (CCBF) は、複数のエージェントが協調して安全性を保証するためのCBFの拡張です。エージェント $i$ のCCBF $h_i(x_i, x_{-i})$ は、エージェント $i$ の状態 $x_i$ だけでなく、他のエージェント $j \in \mathcal{N}_i$ の状態 $x_{-i} = \{x_j : j \in \mathcal{N}_i\}$ にも依存します。

CCBFの定義は以下の通りです：$h_i(x_i, x_{-i})$ がエージェント $i$ のCCBFであるとは、すべての $(x_i, x_{-i}) \in \mathcal{D}_i$ に対して、エージェント $i$ の制御入力 $u_i$ と近傍エージェント $j \in \mathcal{N}_i$ の制御入力 $u_j$ が存在し、以下を満たすことです：

$$\mathcal{L}_{f_i} h_i(x_i, x_{-i}) + \mathcal{L}_{g_i} h_i(x_i, x_{-i}) u_i + \sum_{j \in \mathcal{N}_i} \mathcal{L}_{f_j} h_i(x_i, x_{-i}) + \mathcal{L}_{g_j} h_i(x_i, x_{-i}) u_j + \alpha(h_i(x_i, x_{-i})) \geq 0$$

ここで、$\mathcal{L}_{f_i} h_i$ と $\mathcal{L}_{g_i} h_i$ はそれぞれ $h_i$ の $f_i$ と $g_i$ に関するリー微分、$\mathcal{L}_{f_j} h_i$ と $\mathcal{L}_{g_j} h_i$ はそれぞれ $h_i$ の $f_j$ と $g_j$ に関するリー微分です。

CCBFの重要な性質は、各エージェントが自身のCCBF条件を満たすように制御入力を選択すれば、システム全体の安全性が保証されることです。具体的には、すべてのエージェント $i$ に対して $h_i(x_i, x_{-i}) \geq 0$ が成り立つ初期状態から出発すると、適切な制御入力の下で $h_i(x_i, x_{-i}) \geq 0$ がすべての時刻で保たれます。

### 3.2 SE(3)上のCCBFの具体例

SE(3)上のCCBFの具体例として、複数のドローンが衝突を回避しながら協調して飛行するためのCCBFを考えます。エージェント $i$ と $j$ の間の衝突回避CCBFは以下のように定義できます：

$$h_{ij}(X_i, X_j) = \|p_i - p_j\|^2 - d_{\text{safe}}^2$$

ここで、$p_i$ と $p_j$ はそれぞれエージェント $i$ と $j$ の位置、$d_{\text{safe}}$ は安全距離です。$h_{ij}(X_i, X_j) \geq 0$ を満たす状態は、エージェント $i$ と $j$ が安全距離以上離れていることを意味します。

また、複数のドローンが協調して特定のターゲットを視野内に保つためのCCBFは以下のように定義できます：

$$h_{i,\text{cov}}(X_i, X_j) = n_{ij} - n_{\text{min}}$$

ここで、$n_{ij}$ はエージェント $i$ と $j$ が共有する特徴点の数、$n_{\text{min}}$ は必要最小限の共有特徴点数です。$h_{i,\text{cov}}(X_i, X_j) \geq 0$ を満たす状態は、エージェント $i$ と $j$ が十分な数の特徴点を共有していることを意味します。

### 3.3 SE(3)上のCCBFの微分

SE(3)上のCCBF $h_i(X_i, X_j)$ のリー微分を計算するには、$h_i$ の $X_i$ と $X_j$ に関する勾配を計算し、それぞれのダイナミクスとの内積を取ります。

例えば、衝突回避CCBF $h_{ij}(X_i, X_j) = \|p_i - p_j\|^2 - d_{\text{safe}}^2$ の勾配は：

$$\frac{\partial h_{ij}}{\partial R_i} = 0, \quad \frac{\partial h_{ij}}{\partial p_i} = 2(p_i - p_j)$$
$$\frac{\partial h_{ij}}{\partial R_j} = 0, \quad \frac{\partial h_{ij}}{\partial p_j} = 2(p_j - p_i)$$

これらの勾配を用いて、CCBFのリー微分を計算できます。

## 4. SE(3)上のCCBF制約付きMPC問題の定式化

### 4.1 問題設定

SE(3)上のCCBF制約付きMPC問題は、以下のように定式化できます：

$$\min_{u_i(0), \ldots, u_i(N-1)} \sum_{k=0}^{N-1} \ell_i(X_i(k), \xi_i(k), u_i(k)) + \ell_{i,f}(X_i(N), \xi_i(N))$$

制約条件：
$$X_i(k+1) = X_i(k) \exp(\Delta t \xi_i(k)^\wedge)$$
$$\xi_i(k+1) = f_i(X_i(k), \xi_i(k), u_i(k))$$
$$X_i(0) = X_{i,\text{current}}, \quad \xi_i(0) = \xi_{i,\text{current}}$$
$$u_{i,\text{min}} \leq u_i(k) \leq u_{i,\text{max}}, \quad k = 0, \ldots, N-1$$
$$h_i(X_i(k), X_j(k)) \geq 0, \quad j \in \mathcal{N}_i, \quad k = 0, \ldots, N$$

ここで：
- $\ell_i$ はステージコスト関数
- $\ell_{i,f}$ は終端コスト関数
- $X_i(k)$ と $\xi_i(k)$ はそれぞれ時刻 $k$ におけるエージェント $i$ の状態と速度
- $u_i(k)$ は時刻 $k$ におけるエージェント $i$ の制御入力
- $f_i$ はエージェント $i$ のダイナミクス関数
- $h_i$ はエージェント $i$ のCCBF
- $\mathcal{N}_i$ はエージェント $i$ の近傍エージェントの集合

### 4.2 コスト関数の設計

SE(3)上のMPC問題のコスト関数は、目標状態への追従誤差、制御入力のエネルギー、自己位置推定の不確かさなどを含めることができます。例えば：

$$\ell_i(X_i, \xi_i, u_i) = w_1 d_{SE(3)}(X_i, X_{i,\text{ref}})^2 + w_2 \|\xi_i - \xi_{i,\text{ref}}\|^2 + w_3 \|u_i\|^2 + w_4 \text{tr}(\Sigma_i)$$

ここで：
- $d_{SE(3)}(X_i, X_{i,\text{ref}})$ は $X_i$ と $X_{i,\text{ref}}$ の間のSE(3)上の距離
- $\|\xi_i - \xi_{i,\text{ref}}\|$ は速度の追従誤差
- $\|u_i\|$ は制御入力のノルム
- $\text{tr}(\Sigma_i)$ は自己位置推定の不確かさ（共分散行列のトレース）
- $w_1, w_2, w_3, w_4$ は重み係数

SE(3)上の距離 $d_{SE(3)}(X_1, X_2)$ は、以下のように定義できます：

$$d_{SE(3)}(X_1, X_2) = \|\log(X_1^{-1} X_2)\|$$

ここで、$\log$ はSE(3)からそのリー代数 $\mathfrak{se}(3)$ への対数写像、$\|\cdot\|$ はリー代数上のノルムです。

### 4.3 CCBF制約の離散化

連続時間のCCBF制約を離散時間のMPC問題に組み込むには、離散化が必要です。一般的なアプローチは、以下のような離散時間CBF条件を用いることです：

$$h_i(X_i(k+1), X_j(k+1)) - h_i(X_i(k), X_j(k)) \geq -\gamma h_i(X_i(k), X_j(k))$$

ここで、$\gamma \in (0, 1)$ はCBFパラメータです。この条件は、CBF値が指数関数的に減少することを許容しますが、ゼロ以下にはならないことを保証します。

この離散時間CBF条件を、ダイナミクス方程式を用いて制御入力 $u_i(k)$ と $u_j(k)$ の関数として表現できます。

## 5. SE(3)上のCCBF制約付きMPC問題の解法

### 5.1 リーマン多様体上の最適化

SE(3)上のMPC問題を解くには、リーマン多様体上の最適化手法が必要です。一般的なアプローチは、以下のステップを含みます：

1. 問題をリー代数 $\mathfrak{se}(3)$ 上の最適化問題に変換する
2. リー代数上で最適化アルゴリズム（例：勾配降下法、ニュートン法）を適用する
3. 最適解をリー群 $SE(3)$ に戻す

具体的には、各反復で以下の操作を行います：

1. 現在の推定解 $X^{(k)}$ の周りで目的関数と制約を線形化または二次近似する
2. 接空間（リー代数）上で更新方向 $\delta^{(k)} \in \mathfrak{se}(3)$ を計算する
3. レトラクション操作 $X^{(k+1)} = X^{(k)} \exp(\delta^{(k)})$ で解を更新する

### 5.2 逐次二次計画法（SQP）

SE(3)上のCCBF制約付きMPC問題を解くための効果的な手法の一つは、逐次二次計画法（SQP）です。SQPは、非線形最適化問題を一連の二次計画（QP）問題に近似して解く方法です。

各反復において、現在の推定解の周りで目的関数と制約を二次近似し、QP問題を解いて探索方向を求めます。SE(3)上のSQPでは、リー代数上での二次近似が必要です。

具体的なアルゴリズムは以下の通りです：

1. 初期推定解 $u_i^{(0)} = [u_i^{(0)}(0), \ldots, u_i^{(0)}(N-1)]$ を設定する
2. 反復 $l = 0, 1, 2, \ldots$ に対して：
   a. 現在の推定解 $u_i^{(l)}$ を用いて状態軌道 $X_i^{(l)}(k), \xi_i^{(l)}(k)$ を計算する
   b. 各時刻 $k$ における状態 $X_i^{(l)}(k)$ の周りで目的関数と制約を二次近似する
   c. 近似されたQP問題を解いて探索方向 $\Delta u_i^{(l)}$ を求める
   d. 適切なステップサイズ $\alpha^{(l)}$ を選択する
   e. 推定解を更新する：$u_i^{(l+1)} = u_i^{(l)} + \alpha^{(l)} \Delta u_i^{(l)}$
   f. 収束条件を満たすまで繰り返す

### 5.3 分散実装

CCBF制約付きMPC問題の分散実装では、各エージェントが自身のMPC問題を解き、必要な情報を近傍エージェントと交換します。分散実装の基本的なステップは以下の通りです：

1. 各エージェント $i$ は、センサデータから自身の状態 $X_i$ を推定する
2. 各エージェント $i$ は、近傍エージェント $j \in \mathcal{N}_i$ と通信して、状態情報や補助変数を交換する
3. 各エージェント $i$ は、コンセンサスフィルタを用いて補助変数 $y_i$ を更新する
4. 各エージェント $i$ は、自身のMPC問題を解いて最適制御入力 $u_i$ を計算する
5. 各エージェント $i$ は、計算された制御入力 $u_i$ を実行する
6. 次の時間ステップに進み、ステップ1に戻る

CCBF制約の分散実装では、各エージェントが自身のCCBF条件を満たすように制御入力を選択することで、システム全体の安全性が保証されます。

## 6. 数値例：SE(3)上のCCBF制約付きMPC

### 6.1 問題設定

2台のドローンが協調して特定の軌道を追従する問題を考えます。各ドローンは以下のダイナミクスを持ちます：

$$\dot{R}_i = R_i \omega_i^\wedge$$
$$\dot{p}_i = v_i$$
$$m_i \dot{v}_i = m_i g e_3 + R_i f_i$$
$$J_i \dot{\omega}_i = J_i \omega_i \times \omega_i + \tau_i$$

ドローン間の衝突回避と視野錐台交差を保証するために、以下のCCBF制約を課します：

$$h_{ij}(X_i, X_j) = \|p_i - p_j\|^2 - d_{\text{safe}}^2 \geq 0$$
$$h_{i,\text{cov}}(X_i, X_j) = n_{ij} - n_{\text{min}} \geq 0$$

目標は、これらの安全制約を満たしながら、各ドローンが目標軌道を追従することです。

### 6.2 MPC問題の定式化

各ドローンのMPC問題は以下のように定式化されます：

$$\min_{u_i(0), \ldots, u_i(N-1)} \sum_{k=0}^{N-1} \left( w_1 d_{SE(3)}(X_i(k), X_{i,\text{ref}}(k))^2 + w_2 \|\xi_i(k) - \xi_{i,\text{ref}}(k)\|^2 + w_3 \|u_i(k)\|^2 + w_4 \text{tr}(\Sigma_i(k)) \right)$$

制約条件：
$$X_i(k+1) = X_i(k) \exp(\Delta t \xi_i(k)^\wedge)$$
$$\xi_i(k+1) = f_i(X_i(k), \xi_i(k), u_i(k))$$
$$X_i(0) = X_{i,\text{current}}, \quad \xi_i(0) = \xi_{i,\
