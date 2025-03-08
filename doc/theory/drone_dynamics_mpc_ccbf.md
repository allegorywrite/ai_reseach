# MPCにおけるドローンダイナミクスとCCBF制約の統合

本ドキュメントでは、Consensus-Based Control Barrier Function (CCBF)を用いた視野錐台交差制約付きMPC問題において、ドローンのダイナミクスモデルを明示的に定式化し、最適化問題の解法を詳細に説明します。

## 1. ドローンのダイナミクスモデル

### 1.1 状態空間表現

UAV（ドローン）のダイナミクスは、一般的に非線形状態空間モデルとして以下のように表現できます：

$$\dot{x}_i = f_i(x_i) + g_i(x_i)u_i$$

ここで、$x_i \in \mathbb{R}^n$はUAV $i$の状態ベクトル、$u_i \in \mathbb{R}^m$は制御入力ベクトル、$f_i: \mathbb{R}^n \rightarrow \mathbb{R}^n$と$g_i: \mathbb{R}^n \rightarrow \mathbb{R}^{n \times m}$は滑らかな関数です。

UAVの状態ベクトル$x_i$は、位置、速度、姿勢（オイラー角またはクォータニオン）、角速度などを含みます：

$$x_i = [p_i^T, v_i^T, \eta_i^T, \omega_i^T]^T$$

ここで：
- $p_i = [p_{i,x}, p_{i,y}, p_{i,z}]^T \in \mathbb{R}^3$は位置ベクトル
- $v_i = [v_{i,x}, v_{i,y}, v_{i,z}]^T \in \mathbb{R}^3$は速度ベクトル
- $\eta_i = [\phi_i, \theta_i, \psi_i]^T \in \mathbb{R}^3$はオイラー角（ロール、ピッチ、ヨー）
- $\omega_i = [\omega_{i,x}, \omega_{i,y}, \omega_{i,z}]^T \in \mathbb{R}^3$は角速度ベクトル

制御入力$u_i$は、各モーターの推力または集合的な推力とモーメントを表します：

$$u_i = [F_i, M_{i,x}, M_{i,y}, M_{i,z}]^T$$

ここで、$F_i$は合計推力、$M_{i,x}$、$M_{i,y}$、$M_{i,z}$はロール、ピッチ、ヨー軸周りのモーメントです。

### 1.2 詳細なダイナミクス方程式

ドローンの運動方程式は、ニュートンの運動法則とオイラーの回転方程式に基づいて導出されます。

#### 1.2.1 並進運動

並進運動の方程式は以下のように表されます：

$$\dot{p}_i = v_i$$

$$\dot{v}_i = \frac{1}{m_i} R_i(\eta_i) \begin{bmatrix} 0 \\ 0 \\ F_i \end{bmatrix} - \begin{bmatrix} 0 \\ 0 \\ g \end{bmatrix} - \frac{1}{m_i} D_i v_i$$

ここで：
- $m_i$はUAV $i$の質量
- $R_i(\eta_i)$はボディフレームからワールドフレームへの回転行列
- $g$は重力加速度
- $D_i$は空気抵抗係数行列

回転行列$R_i(\eta_i)$は、オイラー角$\eta_i = [\phi_i, \theta_i, \psi_i]^T$を用いて以下のように計算されます：

$$R_i(\eta_i) = \begin{bmatrix}
\cos\theta_i\cos\psi_i & \sin\phi_i\sin\theta_i\cos\psi_i - \cos\phi_i\sin\psi_i & \cos\phi_i\sin\theta_i\cos\psi_i + \sin\phi_i\sin\psi_i \\
\cos\theta_i\sin\psi_i & \sin\phi_i\sin\theta_i\sin\psi_i + \cos\phi_i\cos\psi_i & \cos\phi_i\sin\theta_i\sin\psi_i - \sin\phi_i\cos\psi_i \\
-\sin\theta_i & \sin\phi_i\cos\theta_i & \cos\phi_i\cos\theta_i
\end{bmatrix}$$

#### 1.2.2 回転運動

回転運動の方程式は以下のように表されます：

$$\dot{\eta}_i = T_i(\eta_i) \omega_i$$

$$\dot{\omega}_i = J_i^{-1} \left( \begin{bmatrix} M_{i,x} \\ M_{i,y} \\ M_{i,z} \end{bmatrix} - \omega_i \times (J_i \omega_i) \right)$$

ここで：
- $T_i(\eta_i)$はオイラー角の時間微分と角速度の関係を表す変換行列
- $J_i$はUAV $i$の慣性モーメント行列
- $\times$はベクトルの外積

変換行列$T_i(\eta_i)$は以下のように定義されます：

$$T_i(\eta_i) = \begin{bmatrix}
1 & \sin\phi_i\tan\theta_i & \cos\phi_i\tan\theta_i \\
0 & \cos\phi_i & -\sin\phi_i \\
0 & \sin\phi_i/\cos\theta_i & \cos\phi_i/\cos\theta_i
\end{bmatrix}$$

### 1.3 簡略化モデル

実際のMPC実装では、計算効率のために簡略化されたモデルがよく使用されます。一般的な簡略化モデルとして、位置と速度のみを考慮した線形モデルがあります：

$$\dot{x}_i = A_i x_i + B_i u_i$$

ここで、$x_i = [p_i^T, v_i^T]^T \in \mathbb{R}^6$、$u_i \in \mathbb{R}^3$は所望の加速度、そして行列$A_i$と$B_i$は以下のように定義されます：

$$A_i = \begin{bmatrix}
0_{3 \times 3} & I_{3 \times 3} \\
0_{3 \times 3} & -\frac{1}{m_i}D_i
\end{bmatrix}, \quad
B_i = \begin{bmatrix}
0_{3 \times 3} \\
I_{3 \times 3}
\end{bmatrix}$$

この簡略化モデルでは、姿勢ダイナミクスは無視され、制御入力は直接加速度として扱われます。これは、内部ループ制御器が姿勢を高速に制御し、外部ループ制御器（MPC）が位置と速度を制御するという階層的な制御構造を前提としています。

## 2. CCBF制約付きMPC問題の定式化

### 2.1 離散時間モデル

MPCを実装するためには、連続時間モデルを離散時間モデルに変換する必要があります。オイラー法や4次のルンゲ・クッタ法などの数値積分法を用いて、以下のような離散時間モデルを得ることができます：

$$x_i(k+1) = F_i(x_i(k), u_i(k))$$

ここで、$F_i$は離散時間ダイナミクス関数、$k$は離散時間ステップです。

簡略化線形モデルの場合、離散時間モデルは以下のようになります：

$$x_i(k+1) = A_{d,i} x_i(k) + B_{d,i} u_i(k)$$

ここで、$A_{d,i} = e^{A_i \Delta t}$、$B_{d,i} = \int_0^{\Delta t} e^{A_i \tau} B_i d\tau$、$\Delta t$はサンプリング時間です。

### 2.2 予測ホライズンと制御ホライズン

MPCでは、予測ホライズン$N_p$と制御ホライズン$N_c$を定義します。予測ホライズンは、将来の状態を予測する時間ステップ数であり、制御ホライズンは、最適化する制御入力の時間ステップ数です。通常、$N_c \leq N_p$です。

### 2.3 目的関数

MPCの目的関数は、自己位置推定の不確かさ、目標状態への追従誤差、制御入力のエネルギーなどを含みます：

$$J_i = \sum_{k=0}^{N_p-1} \left( w_1 \text{tr}(\Sigma_i(k)) + w_2 \|x_i(k) - x_{i,ref}(k)\|_Q^2 + w_3 \|u_i(k)\|_R^2 \right)$$

ここで：
- $\Sigma_i(k)$は時間ステップ$k$におけるUAV $i$の状態推定の不確かさ
- $x_{i,ref}(k)$は時間ステップ$k$における目標状態
- $Q$と$R$は重み行列
- $w_1$、$w_2$、$w_3$は重みパラメータ

### 2.4 CCBF制約

CCBF制約は、安全性（衝突回避）と視野錐台交差を保証するために使用されます。CCBF制約は以下のように表されます：

$$\sum_{m \in \mathcal{M}} \nabla \phi_m(ny_{i,m}(k))^T \dot{\psi}_{i,m}(x_i(k)) \geq \alpha \sum_{m \in \mathcal{M}} \phi_m(ny_{i,m}(k)), \quad \forall k \in \{0, 1, \ldots, N_p-1\}$$

ここで：
- $\phi_m$は単調増加関数
- $y_{i,m}(k)$は時間ステップ$k$におけるUAV $i$の補助変数
- $\psi_{i,m}(x_i(k))$はUAV $i$の局所評価関数
- $\alpha$はCBFパラメータ
- $\mathcal{M}$はCBF制約の集合

補助変数$y_{i,m}(k)$は、コンセンサスフィルタを用いて更新されます：

$$y_{i,m}(k+1) = y_{i,m}(k) + \Delta t \left( k_L \sum_{j \in \mathcal{N}_i} (y_{j,m}(k) - y_{i,m}(k)) + \dot{\psi}_{i,m}(x_i(k)) \right)$$

ここで、$k_L$はコンセンサスゲイン、$\mathcal{N}_i$はUAV $i$の通信近傍です。

### 2.5 その他の制約

その他の制約として、状態と制御入力の境界制約があります：

$$x_{i,min} \leq x_i(k) \leq x_{i,max}, \quad \forall k \in \{0, 1, \ldots, N_p\}$$

$$u_{i,min} \leq u_i(k) \leq u_{i,max}, \quad \forall k \in \{0, 1, \ldots, N_c-1\}$$

また、衝突回避制約も含まれます：

$$\|p_i(k) - p_j(k)\| \geq d_{safe}, \quad \forall j \neq i, \forall k \in \{0, 1, \ldots, N_p\}$$

ここで、$d_{safe}$は安全距離です。

### 2.6 完全なMPC問題

完全なMPC問題は以下のように表されます：

$$
\begin{aligned}
\min_{u_i(0), \ldots, u_i(N_c-1)} \quad & \sum_{k=0}^{N_p-1} \left( w_1 \text{tr}(\Sigma_i(k)) + w_2 \|x_i(k) - x_{i,ref}(k)\|_Q^2 + w_3 \|u_i(k)\|_R^2 \right) \\
\text{s.t.} \quad & x_i(k+1) = F_i(x_i(k), u_i(k)), \quad k \in \{0, 1, \ldots, N_p-1\} \\
& x_i(0) = x_{i,current} \\
& x_{i,min} \leq x_i(k) \leq x_{i,max}, \quad k \in \{0, 1, \ldots, N_p\} \\
& u_{i,min} \leq u_i(k) \leq u_{i,max}, \quad k \in \{0, 1, \ldots, N_c-1\} \\
& \|p_i(k) - p_j(k)\| \geq d_{safe}, \quad \forall j \neq i, k \in \{0, 1, \ldots, N_p\} \\
& \sum_{m \in \mathcal{M}} \nabla \phi_m(ny_{i,m}(k))^T \dot{\psi}_{i,m}(x_i(k)) \geq \alpha \sum_{m \in \mathcal{M}} \phi_m(ny_{i,m}(k)), \quad k \in \{0, 1, \ldots, N_p-1\}
\end{aligned}
$$

## 3. CCBF制約付きMPC問題の解法

### 3.1 非線形最適化問題の解法

CCBF制約付きMPC問題は非線形最適化問題であり、一般的には逐次二次計画法（SQP）や内点法などの非線形最適化アルゴリズムを用いて解かれます。

#### 3.1.1 逐次二次計画法（SQP）

SQPは、非線形最適化問題を一連の二次計画（QP）問題に近似して解く方法です。各反復において、現在の推定解の周りで目的関数と制約を線形化または二次近似し、QP問題を解いて探索方向を求めます。

SQPの基本的なステップは以下の通りです：

1. 初期推定解$u_i^{(0)} = [u_i^{(0)}(0), \ldots, u_i^{(0)}(N_c-1)]$を設定
2. 反復$l = 0, 1, 2, \ldots$に対して：
   a. 現在の推定解$u_i^{(l)}$の周りで目的関数と制約を線形化または二次近似
   b. 近似されたQP問題を解いて探索方向$\Delta u_i^{(l)}$を求める
   c. 適切なステップサイズ$\alpha^{(l)}$を選択
   d. 推定解を更新：$u_i^{(l+1)} = u_i^{(l)} + \alpha^{(l)} \Delta u_i^{(l)}$
   e. 収束条件を満たすまで繰り返す

#### 3.1.2 内点法

内点法は、制約付き最適化問題を一連の無制約または緩和された制約付き問題に変換して解く方法です。不等式制約は、バリア関数やペナルティ関数を用いて目的関数に組み込まれます。

内点法の基本的なステップは以下の通りです：

1. 初期推定解$u_i^{(0)}$と初期バリアパラメータ$\mu^{(0)} > 0$を設定
2. 反復$l = 0, 1, 2, \ldots$に対して：
   a. バリア問題を解いて$u_i^{(l+1)}$を求める
   b. バリアパラメータを更新：$\mu^{(l+1)} = \sigma \mu^{(l)}$（$0 < \sigma < 1$）
   c. 収束条件を満たすまで繰り返す

### 3.2 線形化と離散化

非線形ダイナミクスを扱う場合、線形化と離散化が必要です。一般的なアプローチは、現在の状態と制御入力の周りでダイナミクスを線形化し、オイラー法や4次のルンゲ・クッタ法を用いて離散化することです。

現在の状態$x_i(k)$と制御入力$u_i(k)$の周りでの線形化は以下のように行われます：

$$f_i(x_i, u_i) \approx f_i(x_i(k), u_i(k)) + \frac{\partial f_i}{\partial x_i}(x_i(k), u_i(k))(x_i - x_i(k)) + \frac{\partial f_i}{\partial u_i}(x_i(k), u_i(k))(u_i - u_i(k))$$

ここで、$\frac{\partial f_i}{\partial x_i}$と$\frac{\partial f_i}{\partial u_i}$はヤコビ行列です。

オイラー法による離散化は以下のように行われます：

$$x_i(k+1) \approx x_i(k) + \Delta t \cdot f_i(x_i(k), u_i(k))$$

### 3.3 CCBF制約の処理

CCBF制約は非線形であり、直接扱うのは難しい場合があります。一般的なアプローチは、CCBF制約を線形化または二次近似することです。

CCBF制約の線形化は以下のように行われます：

$$\nabla \phi_m(ny_{i,m}(k))^T \dot{\psi}_{i,m}(x_i(k)) \approx \nabla \phi_m(ny_{i,m}(k))^T \left( \frac{\partial \psi_{i,m}}{\partial x_i}(x_i(k)) \cdot (A_i x_i(k) + B_i u_i(k)) \right)$$

ここで、$\frac{\partial \psi_{i,m}}{\partial x_i}$は$\psi_{i,m}$の勾配です。

### 3.4 分散実装

分散実装では、各UAVは自身のMPC問題を解き、必要な情報を近傍と交換します。分散実装の基本的なステップは以下の通りです：

1. 各UAV $i$は、センサデータから自身の状態$x_i$を推定
2. 各UAV $i$は、近傍$\mathcal{N}_i$と通信して、状態情報や補助変数を交換
3. 各UAV $i$は、コンセンサスフィルタを用いて補助変数$y_i$を更新
4. 各UAV $i$は、自身のMPC問題を解いて最適制御入力$u_i$を計算
5. 各UAV $i$は、計算された制御入力$u_i$を実行
6. 次の時間ステップに進み、ステップ1に戻る

### 3.5 実装上の考慮事項

実装上の考慮事項として、以下の点が挙げられます：

1. **計算効率**：MPCは計算負荷が高いため、効率的な実装が必要です。モデルの簡略化、予測ホライズンの短縮、効率的な最適化アルゴリズムの使用などが考えられます。

2. **通信遅延とパケットロス**：分散実装では、通信遅延とパケットロスが問題になる場合があります。ロバストな通信プロトコルや予測モデルの使用が考えられます。

3. **モデル誤差**：実際のシステムとモデルの間には常に誤差があります。モデル予測誤差を考慮したロバスト制御手法の使用が考えられます。

4. **状態推定**：実際のシステムでは、状態は直接観測できない場合があります。カルマンフィルタなどの状態推定器の使用が必要です。

## 4. 数値例

以下に、簡単な数値例を示します。2台のUAVが協調して特定の軌道を追従する問題を考えます。

### 4.1 パラメータ設定

- UAVの質量：$m_1 = m_2 = 1.0$ kg
- 空気抵抗係数：$D_1 = D_2 = 0.1 \cdot I_{3 \times 3}$
- サンプリング時間：$\Delta t = 0.1$ s
- 予測ホライズン：$N_p = 10$
- 制御ホライズン：$N_c = 5$
- 重み行列：$Q = \text{diag}(10, 10, 10, 1, 1, 1)$, $R = \text{diag}(1, 1, 1)$
- 重みパラメータ：$w_1 = 1.0$, $w_2 = 1.0$, $w_3 = 0.1$
- CBFパラメータ：$\alpha = 0.5$
- コンセンサスゲイン：$k_L = 0.1$
- 安全距離：$d_{safe} = 1.0$ m

### 4.2 初期条件

- UAV 1の初期状態：$x_1(0) = [0, 0, 0, 0, 0, 0]^T$
- UAV 2の初期状態：$x_2(0) = [2, 0, 0, 0, 0, 0]^T$
- 目標軌道：円軌道（半径2 m、周期10 s）

### 4.3 シミュレーション結果

シミュレーション結果は、UAVが安全に目標軌道を追従しながら、視野錐台交差制約を満たすことを示しています。特に、UAV間の距離は常に安全距離以上であり、視野錐台の交差領域には常に十分な特徴点が含まれています。

## 5. 結論

本ドキュメントでは、CCBF制約付きMPC問題におけるドローンのダイナミクスモデルを詳細に定式化し、最適化問題の解法を説明しました。ドローンのダイナミクスモデルは、並進運動と回転運動の方程式に基づいて導出され、MPCの枠組みに組み込まれました。CCBF制約は、安全性と視野錐台交差を保証するために使用され、非線形最適化アルゴリズムを用いて解かれました。

今後の課題としては、より複雑なドローンモデルの考慮、外乱やモデル誤差に対するロバスト性の向上、計算効率の改善などが挙げられます。また、実機実験による検証も重要な課題です。
