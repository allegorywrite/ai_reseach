# サーベイリクエスト: 視野錐台交差制約の高度な定式化に関する理論的検証

## 背景

複数のUAVによる協調的なvisual-inertial SLAMシステムにおいて、視野錐台の交差を維持するためのactive perceptionアプローチを研究しています。特に、Consensus-Based Control Barrier Function (CCBF)を用いて、エージェント間の視野錐台の交差を保証しながら、安全性（衝突回避）も同時に確保する制御手法の開発を目指しています。

最近、CCBFにおける視野錐台交差制約の高度な定式化を提案しましたが、その定式化が理論的に正しいかどうか、また最新の研究成果と整合しているかどうかを検証する必要があります。特に、以下の3つの要素について詳細なサーベイが必要です：

1. オクルージョンを考慮した視野錐台交差制約
2. 協調自己位置推定のための十分な特徴点共有の定量化
3. 自己位置推定の不確かさを最小化する目的関数

## サーベイの目的

本サーベイの目的は、提案した定式化が理論的に正しいかどうか、また最新の研究成果と整合しているかどうかを検証することです。具体的には、以下の点について調査してください：

1. **オクルージョンを考慮した視野錐台交差制約**
   - オクルージョンのモデル化に関する既存研究
   - 視野錐台交差制約にオクルージョンを組み込む手法
   - オクルージョン回避のためのバリア関数の設計
   - オクルージョン平面からの距離に基づく効率的な計算手法

2. **協調自己位置推定のための十分な特徴点共有の定量化**
   - 特徴点共有の定量化に関する既存研究
   - 共有特徴点の数、空間的分散、観測品質の評価手法
   - 協調自己位置推定に必要な「十分な」特徴点共有の定義
   - 特徴点共有を保証するためのバリア関数の設計

3. **自己位置推定の不確かさを最小化する目的関数**
   - 視覚慣性SLAMにおける不確かさモデルに関する既存研究
   - 不確かさを最小化する目的関数の設計
   - 目標状態追従と不確かさ最小化のバランスを取る手法
   - 不確かさを考慮したMPC問題の定式化

## 提案した定式化の概要

以下に、提案した定式化の概要を示します。これらの定式化が理論的に正しいかどうか、また最新の研究成果と整合しているかどうかを検証してください。

### オクルージョンを考慮した視認性関数

```
v_i(l) = 
\begin{cases}
1 & \text{if } r_{min} \leq \|p_i - l\| \leq r_{max} \text{ and } \frac{(l - p_i)^T d_i}{\|l - p_i\|} \geq \cos(\theta/2) \text{ and } o_i(l) = 0 \\
0 & \text{otherwise}
\end{cases}
```

ここで、$o_i(l)$ はUAV $i$ から特徴点 $l$ へのオクルージョン状態を表します。

### オクルージョン回避のためのバリア関数

```
h_{ij}^{occlusion}(x_i, x_j) = \sum_{l \in \mathcal{L}} w_l (1 - o_i(l))(1 - o_j(l))v_i(l)v_j(l)
```

### 十分な特徴点共有のためのバリア関数

```
h_{ij}^{feature}(x_i, x_j) = w_1 (n_{ij} - n_{min}) + w_2 (\det(\Sigma_{ij}) - \sigma_{min}) + w_3 (Q_{ij} - q_{min})
```

ここで、$n_{ij}$ は共有特徴点の数、$\Sigma_{ij}$ は共有特徴点の共分散行列、$Q_{ij}$ は共有特徴点の平均観測品質です。

### 自己位置推定の不確かさモデル

```
\Sigma_i = \left( \sum_{l \in \mathcal{L}} v_i(l) q_i(l) J_l J_l^T \right)^{-1}
```

### 不確かさを最小化する目的関数

```
J_{uncertainty}(x_1, x_2, \ldots, x_N) = \sum_{i=1}^{N} \text{tr}(\Sigma_i) - \sum_{i=1}^{N-1} \sum_{j=i+1}^{N} \text{tr}(\Sigma_{ij})
```

## 期待される成果

1. 提案した定式化が理論的に正しいかどうかの評価
2. 最新の研究成果との比較
3. 定式化の改善点や拡張の可能性
4. 実装上の課題と解決策

## 参考文献

以下の文献を参考にしてください。ただし、これらに限定せず、関連する最新の研究成果も調査してください。

1. Machida, M., & Ichien, M. (2021). Consensus-Based Control Barrier Function for Swarm. In 2021 IEEE International Conference on Robotics and Automation (ICRA) (pp. 8623-8628).
2. Cadena, C., Carlone, L., Carrillo, H., Latif, Y., Scaramuzza, D., Neira, J., ... & Leonard, J. J. (2016). Past, present, and future of simultaneous localization and mapping: Toward the robust-perception age. IEEE Transactions on robotics, 32(6), 1309-1332.
3. Schmuck, P., & Chli, M. (2018). CCM-SLAM: Robust and efficient centralized collaborative monocular simultaneous localization and mapping for robotic teams. Journal of Field Robotics, 35(2), 281-304.
4. Campos-Macías, L., Gómez-Gutiérrez, D., Aldana-López, R., de la Guardia, R., & Parra-Vilchis, J. I. (2021). A hybrid method for online trajectory planning of mobile robots in cluttered environments. IEEE Robotics and Automation Letters, 6(2), 3513-3520.
5. Kaess, M., Johannsson, H., Roberts, R., Ila, V., Leonard, J. J., & Dellaert, F. (2012). iSAM2: Incremental smoothing and mapping using the Bayes tree. The International Journal of Robotics Research, 31(2), 216-235.
