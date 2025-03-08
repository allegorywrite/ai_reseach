# Control Barrier Functions (CBF)の理論

## 1. 基本概念

### 1.1 安全集合と障壁関数

制御システムにおいて、安全性を保証するための手法としてControl Barrier Functions (CBF)が提案されている。システムの状態 $x \in \mathcal{X} \subset \mathbb{R}^n$ に対して、安全集合 $\mathcal{C} \subset \mathbb{R}^n$ を以下のように定義する：

$$\mathcal{C} = \{x \in \mathbb{R}^n : h(x) \geq 0\}$$

ここで、$h: \mathbb{R}^n \rightarrow \mathbb{R}$ は連続微分可能な関数であり、障壁関数（barrier function）と呼ばれる。安全集合 $\mathcal{C}$ の境界 $\partial\mathcal{C}$ と内部 $\text{Int}(\mathcal{C})$ は以下のように表される：

$$\partial\mathcal{C} = \{x \in \mathbb{R}^n : h(x) = 0\}$$
$$\text{Int}(\mathcal{C}) = \{x \in \mathbb{R}^n : h(x) > 0\}$$

### 1.2 制御アフィンシステム

制御アフィンシステムは以下の形式で表される：

$$\dot{x} = f(x) + g(x)u$$

ここで、$f: \mathbb{R}^n \rightarrow \mathbb{R}^n$ と $g: \mathbb{R}^n \rightarrow \mathbb{R}^{n \times m}$ は局所Lipschitz連続な関数であり、$u \in \mathcal{U} \subset \mathbb{R}^m$ は制御入力である。

## 2. Control Barrier Functions (CBF)の定義

### 2.1 ゼロ制御CBF条件

関数 $h: \mathbb{R}^n \rightarrow \mathbb{R}$ が与えられたとき、以下の条件を満たす場合、$h$ はゼロ制御CBF（Zero Control CBF, ZCBF）と呼ばれる：

$$\sup_{u \in \mathcal{U}} [L_f h(x) + L_g h(x)u] \geq -\alpha(h(x)) \quad \forall x \in \mathcal{C}$$

ここで、$L_f h(x) = \frac{\partial h}{\partial x}f(x)$ と $L_g h(x) = \frac{\partial h}{\partial x}g(x)$ はそれぞれLie微分を表し、$\alpha$ は拡張クラス $\mathcal{K}$ 関数（連続、厳密に増加、$\alpha(0) = 0$）である。

### 2.2 高階CBF

システムの相対次数が1より大きい場合、高階CBFが必要となる。$h(x)$ の相対次数が $r$ であるとき、以下の条件を満たす場合、$h$ は高階CBF（High-Order CBF, HOCBF）と呼ばれる：

$$L_f^r h(x) + L_g L_f^{r-1} h(x)u + \alpha_r(\psi_{r-1}(x)) \geq 0 \quad \forall x \in \mathcal{C}_r$$

ここで、$L_f^r h(x)$ は $h(x)$ の $f$ に関する $r$ 階のLie微分を表し、$\psi_{r-1}(x)$ は以下のように定義される：

$$\psi_0(x) = h(x)$$
$$\psi_i(x) = \dot{\psi}_{i-1}(x) + \alpha_i(\psi_{i-1}(x)), \quad i = 1, 2, \ldots, r-1$$

また、$\mathcal{C}_r$ は以下のように定義される：

$$\mathcal{C}_r = \{x \in \mathbb{R}^n : \psi_{r-1}(x) \geq 0\}$$

## 3. CBFに基づく制御設計

### 3.1 CBF制約付き最適制御問題

CBFを用いた安全性保証のための制御入力は、以下の最適化問題の解として得られる：

$$\begin{aligned}
\min_{u \in \mathcal{U}} \quad & \frac{1}{2} \|u - u_{\text{ref}}(x)\|^2 \\
\text{s.t.} \quad & L_f h(x) + L_g h(x)u + \alpha(h(x)) \geq 0
\end{aligned}$$

ここで、$u_{\text{ref}}(x)$ は参照制御入力（例えば、タスク達成のための制御則）である。この最適化問題は、安全性制約を満たしながら、参照制御入力にできるだけ近い制御入力を求めるものである。

### 3.2 複数のCBF制約

複数の安全制約 $h_i(x) \geq 0, i = 1, 2, \ldots, p$ がある場合、最適化問題は以下のように拡張される：

$$\begin{aligned}
\min_{u \in \mathcal{U}} \quad & \frac{1}{2} \|u - u_{\text{ref}}(x)\|^2 \\
\text{s.t.} \quad & L_f h_i(x) + L_g h_i(x)u + \alpha_i(h_i(x)) \geq 0, \quad i = 1, 2, \ldots, p
\end{aligned}$$

## 4. 視野制約へのCBFの応用

### 4.1 カメラの視野制約

カメラの視野（Field of View, FOV）制約は、対象物体がカメラの視野内に収まることを保証するものである。対象物体の位置を $p_{\text{obj}} \in \mathbb{R}^3$ とし、カメラの位置と姿勢をそれぞれ $p_{\text{cam}} \in \mathbb{R}^3$ と $R_{\text{cam}} \in SO(3)$ とする。

カメラ座標系における対象物体の位置 $p_{\text{obj}}^{\text{cam}}$ は以下のように表される：

$$p_{\text{obj}}^{\text{cam}} = R_{\text{cam}}^T (p_{\text{obj}} - p_{\text{cam}})$$

カメラの視野制約は、以下の条件で表される：

$$\begin{aligned}
-\tan(\theta_h/2) \leq \frac{p_{\text{obj},x}^{\text{cam}}}{p_{\text{obj},z}^{\text{cam}}} \leq \tan(\theta_h/2) \\
-\tan(\theta_v/2) \leq \frac{p_{\text{obj},y}^{\text{cam}}}{p_{\text{obj},z}^{\text{cam}}} \leq \tan(\theta_v/2) \\
p_{\text{obj},z}^{\text{cam}} > 0
\end{aligned}$$

ここで、$\theta_h$ と $\theta_v$ はそれぞれカメラの水平視野角と垂直視野角である。

### 4.2 視野制約のためのCBF

視野制約をCBFとして定式化するために、以下の障壁関数を定義する：

$$\begin{aligned}
h_1(x) &= \tan(\theta_h/2) \cdot p_{\text{obj},z}^{\text{cam}} - p_{\text{obj},x}^{\text{cam}} \\
h_2(x) &= \tan(\theta_h/2) \cdot p_{\text{obj},z}^{\text{cam}} + p_{\text{obj},x}^{\text{cam}} \\
h_3(x) &= \tan(\theta_v/2) \cdot p_{\text{obj},z}^{\text{cam}} - p_{\text{obj},y}^{\text{cam}} \\
h_4(x) &= \tan(\theta_v/2) \cdot p_{\text{obj},z}^{\text{cam}} + p_{\text{obj},y}^{\text{cam}} \\
h_5(x) &= p_{\text{obj},z}^{\text{cam}}
\end{aligned}$$

これらの障壁関数に対してCBF制約を適用することで、対象物体がカメラの視野内に収まることを保証できる。

## 5. 複数UAVの視野錐台交差のためのCBF

### 5.1 視野錐台交差の定式化

2台のUAV（UAV1とUAV2）の視野錐台が交差するための条件を考える。各UAVの位置と姿勢をそれぞれ $p_i \in \mathbb{R}^3$ と $R_i \in SO(3)$ ($i = 1, 2$) とする。

視野錐台の交差を保証するためには、共通の視野領域が存在する必要がある。この条件は、2台のUAVの視野錐台の中心軸の角度差が一定の閾値以下であることと、2台のUAVの距離が適切な範囲内にあることで近似できる。

### 5.2 視野錐台交差のためのCBF

視野錐台の交差を保証するためのCBFとして、以下の障壁関数を定義する：

$$h_{\text{overlap}}(x) = \cos(\theta_{\text{max}}) - \frac{v_1^T v_2}{\|v_1\| \|v_2\|}$$

ここで、$v_i = R_i [0, 0, 1]^T$ ($i = 1, 2$) はカメラの光軸方向を表す単位ベクトルであり、$\theta_{\text{max}}$ は許容される最大角度差である。

また、2台のUAVの距離に関する制約として、以下の障壁関数を定義する：

$$h_{\text{dist}}(x) = d_{\text{max}}^2 - \|p_1 - p_2\|^2$$

ここで、$d_{\text{max}}$ は許容される最大距離である。

これらの障壁関数に対してCBF制約を適用することで、2台のUAVの視野錐台が交差することを保証できる。

## 6. 複数UAVの協調制御のためのCBF

### 6.1 衝突回避のためのCBF

複数のUAV間の衝突を回避するためのCBFとして、以下の障壁関数を定義する：

$$h_{\text{collision}}(x) = \|p_i - p_j\|^2 - d_{\text{safe}}^2$$

ここで、$p_i, p_j \in \mathbb{R}^3$ はそれぞれUAV $i$ とUAV $j$ の位置であり、$d_{\text{safe}}$ は安全距離である。

### 6.2 フォーメーション維持のためのCBF

UAVのフォーメーションを維持するためのCBFとして、以下の障壁関数を定義する：

$$h_{\text{formation}}(x) = \epsilon^2 - \|p_i - p_j - d_{ij}\|^2$$

ここで、$d_{ij} \in \mathbb{R}^3$ はUAV $i$ とUAV $j$ の間の目標相対位置であり、$\epsilon$ は許容誤差である。

## 7. CBFとCLFの統合

### 7.1 Control Lyapunov Functions (CLF)

制御Lyapunov関数（Control Lyapunov Function, CLF）は、システムの安定性を保証するための関数である。関数 $V: \mathbb{R}^n \rightarrow \mathbb{R}_{\geq 0}$ が与えられたとき、以下の条件を満たす場合、$V$ はCLFと呼ばれる：

$$\inf_{u \in \mathcal{U}} [L_f V(x) + L_g V(x)u] \leq -\gamma(V(x)) \quad \forall x \in \mathcal{D} \setminus \{0\}$$

ここで、$\gamma$ は拡張クラス $\mathcal{K}$ 関数であり、$\mathcal{D} \subset \mathbb{R}^n$ はシステムの動作領域である。

### 7.2 CLF-CBF-QP

CLFとCBFを統合した制御設計手法として、CLF-CBF-QP（Quadratic Programming）が提案されている。この手法では、以下の最適化問題を解くことで制御入力を求める：

$$\begin{aligned}
\min_{u \in \mathcal{U}, \delta \in \mathbb{R}} \quad & \frac{1}{2} \|u\|^2 + p \delta^2 \\
\text{s.t.} \quad & L_f V(x) + L_g V(x)u \leq -\gamma(V(x)) + \delta \\
& L_f h_i(x) + L_g h_i(x)u + \alpha_i(h_i(x)) \geq 0, \quad i = 1, 2, \ldots, p
\end{aligned}$$

ここで、$\delta$ はCLF制約の緩和変数であり、$p > 0$ は緩和のペナルティ係数である。この最適化問題は、安全性制約を満たしながら、システムの安定性を保証する制御入力を求めるものである。

## 8. 結論と今後の課題

Control Barrier Functions (CBF)は、制御システムの安全性を保証するための強力なツールである。特に、複数のUAVによる協調的なvisual-inertial SLAMシステムにおいて、視野錐台の交差を維持するためのactive perceptionアプローチとして、CBFは有効な手法となり得る。

今後の課題としては、以下が挙げられる：

1. 実際のUAVシステムにおけるCBFの実装と検証
2. 視野錐台交差のためのより精密なCBFの設計
3. 不確かさや外乱に対するロバスト性の向上
4. 計算効率の改善（リアルタイム制御のため）

これらの課題に取り組むことで、複数UAVによる協調的なvisual-inertial SLAMシステムの性能向上が期待される。

## 参考文献

1. A. D. Ames, X. Xu, J. W. Grizzle, and P. Tabuada, "Control Barrier Function Based Quadratic Programs for Safety Critical Systems," IEEE Transactions on Automatic Control, vol. 62, no. 8, pp. 3861-3876, 2017.

2. A. D. Ames, S. Coogan, M. Egerstedt, G. Notomista, K. Sreenath, and P. Tabuada, "Control Barrier Functions: Theory and Applications," European Control Conference (ECC), pp. 3420-3431, 2019.

3. W. Xiao and C. Belta, "Control Barrier Functions for Systems with High Relative Degree," IEEE Conference on Decision and Control (CDC), pp. 474-479, 2019.

4. L. Wang, A. D. Ames, and M. Egerstedt, "Safety Barrier Certificates for Collisions-Free Multirobot Systems," IEEE Transactions on Robotics, vol. 33, no. 3, pp. 661-674, 2017.

5. D. Falanga, P. Foehn, P. Lu, and D. Scaramuzza, "PAMPC: Perception-Aware Model Predictive Control for Quadrotors," IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 1-8, 2018.

6. B. Trimarchi, M. Giammarino, S. Gros, and P. Falcone, "A CBF Candidate for Limited FOV Sensors," arXiv preprint arXiv:2410.01277, 2024.
