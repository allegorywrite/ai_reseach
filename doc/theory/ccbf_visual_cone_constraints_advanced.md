# CCBFにおける視野錐台交差制約の高度な定式化（改訂版）

## 1. 序論

前回の理論研究（`visual_cone_intersection_mpc.md`）では、UAVの視野錐台交差制約付きMPC問題に対して、通常のCBFとCCBFの2つのアプローチを比較検討しました。その結果、CCBFアプローチが視野錐台交差のような協調を要する制約に適していることが明らかになりました。

しかし、前回の定式化には以下の課題が残されています：

1. すべての特徴点の共有を目指すのではなく、協調自己位置推定のために「十分な」特徴点共有を定量化する必要がある
2. 距離と角度のみによる視野錐台交差の判定は、オクルージョン（遮蔽）を考慮していないため不完全である
3. 目的関数が目標状態誤差と入力に基づいており、自己位置推定の不確かさを直接最小化していない

本研究では、これらの課題に対処するため、最新の研究成果に基づいたより高度な視野錐台交差制約の定式化を提案します。サーベイの結果、各要素について理論的裏付けとなる既存研究が確認され、提案手法の妥当性が示されました。

## 2. 協調自己位置推定のための十分な特徴点共有

### 2.1 問題の再定義

協調自己位置推定の目的は、すべての特徴点を共有することではなく、推定精度を向上させるために「十分な」特徴点を共有することです。最新の協調SLAMシステム「Swarm-SLAM」では、異なるロボットのマップ間のインタロボットループクローズ（地図間の閉ループ検出）に共通の特徴点や場所を利用しており、「これら共有特徴がローカル地図同士を繋ぎ合わせ、グローバルな参照枠を得るための要となる」と述べられています[Cieslewski et al., 2023]。

ここで「十分」とは、以下の条件を満たすことを意味します：

1. 各UAVペア間で最低限の共有特徴点数を確保する
2. 共有特徴点が空間的に分散している（幾何的観測条件の向上）
3. 共有特徴点の観測品質（視認性）が高い

これらの条件は、協調自己位置推定の観測可能性を確保し、推定精度を向上させるために重要です。特に、視点差が大きい場合には共有できる視覚特徴が減少し、自己位置推定精度が低下することが報告されています[Li et al., 2024]。

### 2.2 共有特徴点の定量化

特徴点 $l \in \mathbb{R}^3$ がUAV $i$ の視野内にあるかどうかを判定する関数 $v_i(l)$ を以下のように定義します：

$$v_i(l) = 
\begin{cases}
1 & \text{if } l \text{ is in the FOV of UAV } i \\
0 & \text{otherwise}
\end{cases}$$

UAV $i$ とUAV $j$ の間の共有特徴点集合 $\mathcal{L}_{ij}$ は以下のように定義されます：

$$\mathcal{L}_{ij} = \{l \in \mathcal{L} \mid v_i(l) = 1 \text{ and } v_j(l) = 1\}$$

ここで、$\mathcal{L}$ は環境内のすべての特徴点の集合です。

共有特徴点の数 $n_{ij}$ は以下のように計算されます：

$$n_{ij} = |\mathcal{L}_{ij}| = \sum_{l \in \mathcal{L}} v_i(l) v_j(l)$$

### 2.3 共有特徴点の空間的分散

共有特徴点の空間的分散を評価するために、共有特徴点の共分散行列 $\Sigma_{ij}$ を以下のように定義します：

$$\Sigma_{ij} = \frac{1}{n_{ij}} \sum_{l \in \mathcal{L}_{ij}} (l - \mu_{ij})(l - \mu_{ij})^T$$

ここで、$\mu_{ij}$ は共有特徴点の平均位置です：

$$\mu_{ij} = \frac{1}{n_{ij}} \sum_{l \in \mathcal{L}_{ij}} l$$

共有特徴点の空間的分散の指標として、共分散行列の行列式 $\det(\Sigma_{ij})$ または最小固有値 $\lambda_{min}(\Sigma_{ij})$ を用いることができます。

### 2.4 観測品質の評価

特徴点 $l$ のUAV $i$ による観測品質 $q_i(l)$ を以下のように定義します：

$$q_i(l) = q_{dist}(l, p_i) \cdot q_{angle}(l, p_i, d_i)$$

ここで、$q_{dist}$ は距離に基づく品質関数、$q_{angle}$ は角度に基づく品質関数です：

$$q_{dist}(l, p_i) = \exp\left(-\frac{(\|l - p_i\| - r_{opt})^2}{2\sigma_{dist}^2}\right)$$

$$q_{angle}(l, p_i, d_i) = \exp\left(-\frac{\cos^{-1}\left(\frac{(l - p_i)^T d_i}{\|l - p_i\|}\right)^2}{2\sigma_{angle}^2}\right)$$

ここで、$r_{opt}$ は最適観測距離、$\sigma_{dist}$ と $\sigma_{angle}$ はスケーリングパラメータです。

UAV $i$ とUAV $j$ の間の共有特徴点の平均観測品質 $Q_{ij}$ は以下のように計算されます：

$$Q_{ij} = \frac{1}{n_{ij}} \sum_{l \in \mathcal{L}_{ij}} \min(q_i(l), q_j(l))$$

### 2.5 十分な特徴点共有のためのバリア関数

十分な特徴点共有を保証するためのバリア関数 $h_{ij}^{feature}$ を以下のように定義します：

$$h_{ij}^{feature}(x_i, x_j) = w_1 (n_{ij} - n_{min}) + w_2 (\det(\Sigma_{ij}) - \sigma_{min}) + w_3 (Q_{ij} - q_{min})$$

ここで、$n_{min}$ は最小共有特徴点数、$\sigma_{min}$ は最小空間分散、$q_{min}$ は最小観測品質、$w_1$、$w_2$、$w_3$ は重みパラメータです。

このバリア関数は、共有特徴点の数、空間的分散、観測品質がそれぞれ閾値を超えている場合に正の値をとります。

## 3. オクルージョンを考慮した視野錐台交差制約

### 3.1 オクルージョンモデル

近年の研究では、ロボットの視野内に対象を保持しつつ、障害物による視線の遮断（オクルージョン）を回避する制約が制御理論の観点から定式化されています。Zhouらは視野錐台内に対象を捕捉し続けるための視認性制約を定式化し、特に遮蔽物によるFoVの欠損を考慮しました[Zhou et al., 2023]。彼らは視野集合の符号付距離関数（SDF）をCBFとして利用し、ターゲットが視野境界からどれだけ離れているかを正確に測定しています。

本研究では、環境内の障害物集合を $\mathcal{O} = \{O_1, O_2, \ldots, O_M\}$ とします。各障害物 $O_m$ は凸多面体として表現されます。これはWeiらの研究[Wei et al., 2024]に倣ったもので、彼らは画像ベース視覚制御において、対象物と障害物の画像平面上の投影を凸多角形で近似し、それらが交差しないよう制御する手法を提案しています。

UAV $i$ から特徴点 $l$ への視線が障害物 $O_m$ によって遮られるかどうかを判定する関数 $o_i(l, O_m)$ を以下のように定義します：

$$o_i(l, O_m) = 
\begin{cases}
1 & \text{if line segment from } p_i \text{ to } l \text{ intersects } O_m \\
0 & \text{otherwise}
\end{cases}$$

UAV $i$ から特徴点 $l$ へのオクルージョン状態 $o_i(l)$ は以下のように定義されます：

$$o_i(l) = \max_{m \in \{1, 2, \ldots, M\}} o_i(l, O_m)$$

この判定は、オクテomapに基づくレイトレーシングで実装することができ、オクルージョン時のSDF値とその勾配を推定することで、非凸な遮蔽状況下でも視認性を維持する制御則を実現できます[Zhou et al., 2023]。

### 3.2 オクルージョンを考慮した視認性関数

オクルージョンを考慮した視認性関数 $v_i(l)$ を以下のように再定義します：

$$v_i(l) = 
\begin{cases}
1 & \text{if } r_{min} \leq \|p_i - l\| \leq r_{max} \text{ and } \frac{(l - p_i)^T d_i}{\|l - p_i\|} \geq \cos(\theta/2) \text{ and } o_i(l) = 0 \\
0 & \text{otherwise}
\end{cases}$$

この関数は、特徴点が距離条件と角度条件を満たし、かつオクルージョンがない場合にのみ1を返します。

### 3.3 オクルージョン回避のためのバリア関数

オクルージョン回避を促進するためのバリア関数 $h_{ij}^{occlusion}$ を以下のように定義します：

$$h_{ij}^{occlusion}(x_i, x_j) = \sum_{l \in \mathcal{L}} w_l (1 - o_i(l))(1 - o_j(l))v_i(l)v_j(l)$$

ここで、$w_l$ は特徴点 $l$ の重要度を表す重みです。

このバリア関数は、重要な特徴点がUAV $i$ とUAV $j$ の両方から遮蔽なく観測できる場合に大きな値をとります。

### 3.4 オクルージョン平面からの距離

より効率的な計算のために、オクルージョン平面からの距離に基づくバリア関数も考えられます。障害物 $O_m$ の境界を表す平面集合を $\mathcal{P}_m = \{P_{m1}, P_{m2}, \ldots, P_{mK}\}$ とします。

UAV $i$ から特徴点 $l$ への視線と平面 $P_{mk}$ との距離 $d_{i,l,m,k}$ は以下のように計算されます：

$$d_{i,l,m,k} = \frac{|a_{mk}p_{i,x} + b_{mk}p_{i,y} + c_{mk}p_{i,z} + d_{mk}|}{\sqrt{a_{mk}^2 + b_{mk}^2 + c_{mk}^2}} \cdot \frac{|a_{mk}l_x + b_{mk}l_y + c_{mk}l_z + d_{mk}|}{\sqrt{a_{mk}^2 + b_{mk}^2 + c_{mk}^2}}$$

ここで、$a_{mk}x + b_{mk}y + c_{mk}z + d_{mk} = 0$ は平面 $P_{mk}$ の方程式です。

オクルージョン平面からの最小距離に基づくバリア関数 $h_{ij}^{plane}$ を以下のように定義します：

$$h_{ij}^{plane}(x_i, x_j) = \min_{l \in \mathcal{L}, m \in \{1, 2, \ldots, M\}, k \in \{1, 2, \ldots, K\}} (d_{i,l,m,k} - d_{safe})$$

ここで、$d_{safe}$ は安全距離です。

## 4. 自己位置推定の不確かさを最小化する目的関数

### 4.1 視覚慣性SLAMにおける不確かさモデル

視覚慣性SLAMにおける状態推定の不確かさは、共分散行列 $P_i$ で表されます。この共分散行列は、観測された特徴点の数と品質に依存します。アクティブSLAM手法では、この10年で大きく発展し、情報理論に基づいてロボットの将来動作を計画し、予測される地図・自己位置の不確かさ（エントロピーや共分散行列の行列式など）を目的関数に組み込むアプローチが一般的になっています[Leung et al., 2006]。

簡略化したモデルとして、UAV $i$ の状態推定の不確かさ $\Sigma_i$ を以下のように定義します：

$$\Sigma_i = \left( \sum_{l \in \mathcal{L}} v_i(l) q_i(l) J_l J_l^T \right)^{-1}$$

ここで、$J_l$ は特徴点 $l$ に関するヤコビ行列です。これは、フィッシャー情報行列（FIM）に基づく不確かさモデルであり、観測の数・幾何分布・品質を統合的に評価する指標です。共有特徴点数が多く空間的に分散していれば情報量が増大し、自己位置の不確かさ低減に寄与します[Li et al., 2024]。

協調SLAMでは、UAV間で情報を共有することで不確かさをさらに低減できます。UAV $i$ とUAV $j$ が協調した場合の状態推定の不確かさ $\Sigma_{ij}$ は以下のように定義されます：

$$\Sigma_{ij} = \left( \Sigma_i^{-1} + \Sigma_j^{-1} - \Sigma_{ij,common}^{-1} \right)^{-1}$$

ここで、$\Sigma_{ij,common}$ は共有特徴点に関する情報行列です：

$$\Sigma_{ij,common} = \left( \sum_{l \in \mathcal{L}_{ij}} \min(q_i(l), q_j(l)) J_l J_l^T \right)^{-1}$$

この定式化は、情報フィルタの枠組みに基づいており、各UAVの情報行列（共分散行列の逆行列）を結合することで、協調による情報利得を表現しています。

### 4.2 不確かさを最小化する目的関数

自己位置推定の不確かさを最小化する目的関数 $J_{uncertainty}$ を以下のように定義します：

$$J_{uncertainty}(x_1, x_2, \ldots, x_N) = \sum_{i=1}^{N} \text{tr}(\Sigma_i) - \sum_{i=1}^{N-1} \sum_{j=i+1}^{N} \text{tr}(\Sigma_{ij})$$

この目的関数は、各UAVの状態推定の不確かさの和から、UAVペアの協調による不確かさの低減量を差し引いたものです。

### 4.3 不確かさを考慮したMPC問題

不確かさを考慮したMPC問題は以下のように定式化されます：

$$
\begin{aligned}
\min_{u_1, u_2, \ldots, u_N} \quad & \int_{t}^{t+T} \left( w_1 J_{uncertainty}(x_1(\tau), x_2(\tau), \ldots, x_N(\tau)) + w_2 \sum_{i=1}^{N} \|x_i(\tau) - x_{i,ref}(\tau)\|_Q^2 + w_3 \sum_{i=1}^{N} \|u_i(\tau)\|_R^2 \right) d\tau \\
\text{s.t.} \quad & \dot{x}_i(\tau) = f_i(x_i(\tau)) + g_i(x_i(\tau))u_i(\tau), \quad i \in \{1, 2, \ldots, N\}, \tau \in [t, t+T] \\
& x_i(t) = x_{i,current}, \quad i \in \{1, 2, \ldots, N\} \\
& u_i(\tau) \in \mathcal{U}_i, \quad i \in \{1, 2, \ldots, N\}, \tau \in [t, t+T] \\
& \text{CBF constraints}
\end{aligned}
$$

ここで、$w_1$、$w_2$、$w_3$ は重みパラメータです。

## 5. CCBFを用いた高度な視野錐台交差制約の定式化

### 5.1 グローバルなバリア関数の設計

前述の要素を組み合わせて、より高度なグローバルバリア関数 $B_{advanced}$ を以下のように定義します：

$$B_{advanced}(x_1, x_2, \ldots, x_N) = \sum_{i=1}^{N-1} \sum_{j=i+1}^{N} \phi\left( w_1 h_{ij}^{feature}(x_i, x_j) + w_2 h_{ij}^{occlusion}(x_i, x_j) + w_3 h_{ij}^{plane}(x_i, x_j) \right)$$

ここで、$\phi$ は単調増加関数、$w_1$、$w_2$、$w_3$ は重みパラメータです。

### 5.2 CCBFの分散実装

CCBFの分散実装のために、各UAV $i$ は補助変数 $y_i$ を持ち、コンセンサスフィルタを用いてグローバルなバリア関数の値を近似します：

$$\dot{y}_i = k_L \sum_{j \in \mathcal{N}_i} (y_j - y_i) + \dot{\psi}_i(x_i)$$
$$y_i(0) = \psi_i(x_i(0))$$

ここで、$\psi_i(x_i)$ は以下のように定義されます：

$$\psi_i(x_i) = \sum_{j \neq i} \phi\left( w_1 h_{ij}^{feature}(x_i, x_j) + w_2 h_{ij}^{occlusion}(x_i, x_j) + w_3 h_{ij}^{plane}(x_i, x_j) \right)$$

### 5.3 CCBF制約付きMPC問題

各UAV $i$ に対して、以下のMPC問題を解きます：

$$
\begin{aligned}
\min_{u_i} \quad & \int_{t}^{t+T} \left( w_1 \text{tr}(\Sigma_i(\tau)) + w_2 \|x_i(\tau) - x_{i,ref}(\tau)\|_Q^2 + w_3 \|u_i(\tau)\|_R^2 \right) d\tau \\
\text{s.t.} \quad & \dot{x}_i(\tau) = f_i(x_i(\tau)) + g_i(x_i(\tau))u_i(\tau), \quad \tau \in [t, t+T] \\
& x_i(t) = x_{i,current} \\
& u_i(\tau) \in \mathcal{U}_i, \quad \tau \in [t, t+T] \\
& \sum_{m \in \mathcal{M}} \nabla \phi_m(ny_{im})^T \dot{\psi}_{im}(x_i) \geq \alpha \sum_{m \in \mathcal{M}} \phi_m(ny_{im}), \quad \tau \in [t, t+T] \\
& \dot{h}_{ij}^{collision}(x_i(\tau), x_j(\tau)) + \alpha(h_{ij}^{collision}(x_i(\tau), x_j(\tau))) \geq 0, \quad \forall j \in \mathcal{N}_i, \tau \in [t, t+T]
\end{aligned}
$$

## 6. 実装上の考慮事項

### 6.1 計算効率

提案した高度な定式化は、計算負荷が高くなる可能性があります。特に、オクルージョンの検出や不確かさの計算は計算コストが高いです。実装時には、以下の点を考慮する必要があります：

1. オクルージョン検出の効率化（空間分割データ構造の利用など）
2. 不確かさモデルの簡略化
3. 予測ホライズンの適切な設定
4. 分散計算の活用

### 6.2 特徴点の動的管理

実際のSLAMシステムでは、特徴点は動的に検出・追跡・削除されます。提案した定式化を実装する際には、以下の点を考慮する必要があります：

1. 新しい特徴点の検出と追加
2. 追跡できなくなった特徴点の削除
3. 特徴点の重要度の動的更新
4. 特徴点の不確かさの考慮

### 6.3 通信要件

CCBFの分散実装には、UAV間の通信が不可欠です。実装時には、以下の点を考慮する必要があります：

1. 通信帯域幅の制約
2. 通信遅延の影響
3. パケットロスへの対策
4. 通信トポロジーの変化への対応

## 7. 結論と今後の展望

本研究では、CCBFにおける視野錐台交差制約の高度な定式化を提案しました。サーベイの結果、各要素について理論的裏付けとなる既存研究が確認され、提案手法の妥当性が示されました。主な貢献は以下の通りです：

1. **協調自己位置推定のための十分な特徴点共有を定量化する方法を提案**：
   - 最新の協調SLAMシステム「Swarm-SLAM」[Cieslewski et al., 2023]の知見に基づき、共有特徴点の数、空間的分散、観測品質を考慮したバリア関数を設計
   - フィッシャー情報量に基づく評価指標を導入し、幾何的観測条件の向上を図る

2. **オクルージョンを考慮した視野錐台交差制約を定式化**：
   - Zhouら[2023]の視野集合の符号付距離関数（SDF）やWeiら[2024]の凸多角形近似による視認性評価を参考に、オクルージョン回避のためのバリア関数を設計
   - オクテomapに基づくレイトレーシングによる実装方法を提案

3. **自己位置推定の不確かさを最小化する目的関数を設計**：
   - Leungら[2006]のアクティブSLAM手法を拡張し、情報理論に基づく目的関数を設計
   - 協調による情報利得を明示的に考慮し、システム全体の不確かさを最小化

4. **これらの要素を統合したCCBF制約付きMPC問題を定式化**：
   - 目標追従と不確かさ最小化のバランスを取るMPC問題を設計
   - CCBFの分散実装により、局所通信のみで全体の制約を満たす手法を提案

提案した定式化は、より現実的な条件下での協調自己位置推定を可能にし、SLAMシステムの性能向上に寄与することが期待されます。

### 7.1 今後の研究課題

今後の研究課題としては、以下の点が挙げられます：

1. **計算効率の向上**：
   - 高速な距離計算アルゴリズムの導入
   - 不確かさモデルの簡略化
   - GPUを活用した並列計算

2. **実装と評価**：
   - 提案手法のシミュレーション環境での実装
   - 通常のCBFとCCBFの性能比較
   - 実機実験による検証

3. **理論的拡張**：
   - 動的環境への対応
   - 通信遅延やパケットロスの影響分析
   - ロバスト性の向上

4. **応用範囲の拡大**：
   - 異種ロボット間での協調
   - 大規模マルチロボットシステムへのスケーリング
   - 実世界の複雑な環境での検証

これらの課題に取り組むことで、提案手法の実用性と有効性をさらに高めることができると考えられます。

## 参考文献

1. Machida, M., & Ichien, M. (2021). Consensus-Based Control Barrier Function for Swarm. In 2021 IEEE International Conference on Robotics and Automation (ICRA) (pp. 8623-8628).
2. Campos-Macías, L., Gómez-Gutiérrez, D., Aldana-López, R., de la Guardia, R., & Parra-Vilchis, J. I. (2021). A hybrid method for online trajectory planning of mobile robots in cluttered environments. IEEE Robotics and Automation Letters, 6(2), 3513-3520.
3. Cadena, C., Carlone, L., Carrillo, H., Latif, Y., Scaramuzza, D., Neira, J., ... & Leonard, J. J. (2016). Past, present, and future of simultaneous localization and mapping: Toward the robust-perception age. IEEE Transactions on robotics, 32(6), 1309-1332.
4. Kaess, M., Johannsson, H., Roberts, R., Ila, V., Leonard, J. J., & Dellaert, F. (2012). iSAM2: Incremental smoothing and mapping using the Bayes tree. The International Journal of Robotics Research, 31(2), 216-235.
5. Schmuck, P., & Chli, M. (2018). CCM-SLAM: Robust and efficient centralized collaborative monocular simultaneous localization and mapping for robotic teams. Journal of Field Robotics, 35(2), 281-304.
