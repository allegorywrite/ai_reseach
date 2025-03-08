# ArduPilotおよびPX4におけるMPC・CBF実装の研究事例

オープンソースのフライトコントローラであるArduPilotやPX4は、学術研究において先進的な制御手法を実機に適用するためのプラットフォームとして利用されています。例えば、PX4では**Control Barrier Function (CBF)**を用いた安全フィルタが提案されており、オンボードの距離センサや速度推定を使って、衝突を防ぐように加速度指令をリアルタイムで微調整します​**

**[github.com](https://github.com/ntnu-arl/PX4-CBF#:~:text=This%20repository%20presents%20the%20instructions,acceleration%20setpoint%20to%20prevent%20collisions)**

**。このCBF安全フィルタはPX4の位置・速度制御ループに組み込まれ、最小限の修正で障害物回避を実現しており、実際に小型コンピュータ（PixRacer ProやVOXL2 Mini）上で動作検証されています​

[github.com](https://github.com/ntnu-arl/PX4-CBF#:~:text=The%20unconstrained,resources%20on%20the%20controller%20board)

。一方、ArduPilotではデフォルトでPID制御を採用していますが、そのオープンな構造ゆえに研究者が制御アルゴリズムを拡張しやすく、MPCのような最適制御を適用した事例も報告されています。たとえばAmadiらの研究では、Pixhawk（PX4仕様の飛行コントローラ）上で**Model Predictive Control (MPC)**によりクアッドロータの角速度制御を実装し、シミュレーションおよび実機試験でPID制御と同等以上に安定して姿勢レートを制御できることを示しました​

[matec-conferences.org](https://www.matec-conferences.org/articles/matecconf/pdf/2022/17/matecconf_rapdasa2022_05007.pdf#:~:text=though%20the%20UAV%20used%20is,wing%20UAV%20and%20is%20successful)

。さらに固定翼機の自動着陸研究においても、ロータリー翼でのMPC手法を参考にする例があり、MPCによる軌道追従が現実の飛行体で有効に機能することが確認されています​

[matec-conferences.org](https://www.matec-conferences.org/articles/matecconf/pdf/2022/17/matecconf_rapdasa2022_05007.pdf#:~:text=explores%20using%20MPC%20methods%20to,wing%20UAV%20and%20is%20successful)

。また、ArduPilot自体の制御ループを拡張する研究も行われており、Simone BaldiらはArduPilotのPIDループにモデルフリー適応制御を付加し、ペイロード変化や風ゆらぎに対しても70%以上追従誤差を低減できる適応型オートパイロットを提案しています​

[researchgate.net](https://www.researchgate.net/publication/382288247_MRS_ArduPilot_An_Adaptive_ArduPilot_Architecture_Based_on_Model_Reference_Stabilization#:~:text=This%20article%20presents%20an%20adaptive,attitude%20and%20total%20energy%20control)

​

[researchgate.net](https://www.researchgate.net/publication/382288247_MRS_ArduPilot_An_Adaptive_ArduPilot_Architecture_Based_on_Model_Reference_Stabilization#:~:text=loops,reduced%20control%20effort)

。このように、ArduPilot/PX4を用いた実機実験では、MPCやCBFを組み込んだ高度な制御手法の有効性が学術的に検証されています。

# MPCとCBFを活用した制御手法の理論的研究

MPCとCBFはいずれも制約条件下で安全かつ最適な制御を行うための理論枠組みとして発展してきました。それぞれアプローチは異なりますが、複雑な無人機（ドローン）の制御に応用する研究が盛んです。**MPC**は将来のシステム挙動を予測しつつ最適な入力系列を算出する制御であり、非線形性や入力飽和などを同時に扱えるためクアッドロータの軌道追従にも有効だとされています​

[rpg.ifi.uzh.ch](https://rpg.ifi.uzh.ch/docs/TRO22_MPCC_Romero.pdf#:~:text=Nonlinear%20controllers%20have%20been%20proposed,principle%20models%20%5B27%5D%2C%20Gaussian%02process%20models)

。一方で**Control Barrier Function**を用いた制御は、制御における安全性（状態をある安全集合から外れないこと）を数学的に保証する枠組みです。CBFは制御Lyapunov関数（CLF）と組み合わせて**安全制約を満たす最適制御問題（通常は二次計画問題）**として定式化でき、連続時間系では凸（二次）計画としてリアルタイム解法が可能であることが示されています​

[roboticsproceedings.org](https://roboticsproceedings.org/rss13/p73.pdf#:~:text=gained%20success%20in%20a%20wide,28%5D%2C%20control%20barrier)

。CBFの近年の研究では、障害物回避など安全クリティカルな課題に対し、CLFとCBFを組み合わせたクォードロータ制御が提案されており、システムの状態を安全集合内に保つような最適入力を計算することで安定化と安全性を両立しています​

[roboticsproceedings.org](https://roboticsproceedings.org/rss13/p73.pdf#:~:text=gained%20success%20in%20a%20wide,maintains%20the%20states%20of%20the)

。特に、CBFを取り入れた制御では安全条件が“ハード”な制約として扱われるため、最適化計算が解を得られる限り**安全は保証**されます​

[arxiv.org](https://arxiv.org/pdf/2303.15871#:~:text=situations%20while%20guaranteeing%20safety,dependent%20on%20the%20optimiza%02tion%20algorithm%E2%80%99s)

。これに対しMPC（特に非線形MPC）は制約違反を厳罰項で避ける“ソフト”な取り扱いになる場合も多く、解法アルゴリズムの性能に制約満足度が左右されるため、安全保証という観点ではCBF手法が優位と論じられています​

[arxiv.org](https://arxiv.org/pdf/2303.15871#:~:text=is%20a%20model,NMPC%2C%20on%20the%20other%20hand)

​

[arxiv.org](https://arxiv.org/pdf/2303.15871#:~:text=situations%20while%20guaranteeing%20safety,dependent%20on%20the%20optimiza%02tion%20algorithm%E2%80%99s)

。もっとも、MPCにもロバストMPCやチューブMPCなど安全性・安定性を保証する理論研究があり、CBFとMPCを融合したアプローチ（例えばMPCの制約条件にCBFを組み込むなど）も模索されています。総じて、MPCは最適性能と制約満足を同時に追求する理論、CBFは制御系にハードな安全保証を与える理論として、いずれもドローン制御の高度化に理論面から貢献しています。

# 実機実装における課題と解決策

MPCやCBFによる制御アルゴリズムを実際のドローンに実装する際には、いくつかの実用上の課題が指摘されています。その代表的な課題と対策を以下にまとめます。

- **計算コスト**: オンラインで最適制御問題を解くMPCは計算負荷が高く、小型のフライトコントローラ上でリアルタイム実行するのは困難です​
    
    [arxiv.org](https://arxiv.org/abs/2308.15946#:~:text=,quadcopter%20position%20stabilization%20by%20analyzing)
    
    。この問題への一つの対処法として、**Explicit MPC**（あらかじめ最適解を解析的に計算・テーブル化しておく手法）が研究されています。例えば最近の研究では、クアッドロータの非線形ダイナミクスを**微分フラット性**に基づき平坦化して独立した複数の線形サブシステムに分離し、それぞれに対して離線でMPCの解を計算しておくことで、オンライン計算を不要にする手法が実証されています​
    
    [arxiv.org](https://arxiv.org/abs/2308.15946#:~:text=constraint%20satisfaction%20and%20optimality%2C%20Explicit,The)
    
    ​
    
    [arxiv.org](https://arxiv.org/abs/2308.15946#:~:text=double%20integrators%20at%20a%20price,scalability%20in%20a%20centralized%20manner)
    
    。このExplicit MPCにより、最先端の非線形MPCと同等の性能と制約保証を達成しつつ計算コストを大幅に削減でき、オンボード実装の現実性を高めています​
    
    [arxiv.org](https://arxiv.org/abs/2308.15946#:~:text=double%20integrators%20at%20a%20price,scalability%20in%20a%20centralized%20manner)
    
    。
    
- **制御遅延とループ周波数**: 最適化計算による指令生成には時間がかかるため、処理遅延や制御ループの低下も課題です。ドローンの安定飛行には高速なフィードバックが不可欠であり、例えば画像処理を伴う制御では計算負荷が大きいとループ周波数が10Hz程度に制限され、クアッドロータのような高応答性が要求されるプラットフォームでは不十分となるケースがあります​
    
    [hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ICRA2024_Point_Cloud_CBF.pdf#:~:text=Control%20barrier%20functions%20were%20also,the%20ability%20to%20adapt%20to)
    
    ​
    
    [hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ICRA2024_Point_Cloud_CBF.pdf#:~:text=Current%20safe%20vision,technique%20which%20formulates%20control%20barrier)
    
    。この問題への対策として、計算資源の拡充（高性能なオンボードコンピュータの搭載）や、制御系を階層化して一部演算を低速ループにオフロードする方法があります（※階層型制御は後述）。また、制御遅延そのものをモデルに組み込んで補償する予測制御設計や、最適化のイテレーション打ち切りによる近似解でも安定性を保つようなロバスト設計も検討されています。
    
- **モデル誤差・ロバスト性**: 実機の飛行では空力特性の不確かさやセンサノイズなどモデルと現実の不一致が避けられず、MPCの性能が劣化したり安全性が損なわれる要因になります​
    
    [researchgate.net](https://www.researchgate.net/publication/382288247_MRS_ArduPilot_An_Adaptive_ArduPilot_Architecture_Based_on_Model_Reference_Stabilization#:~:text=revolutionize%20shipping%2C%20transportation%2C%20and%20search,proposed%20architecture%20generalizes%20to%20many)
    
    。この課題に対しては、**適応制御**や**ロバスト制御**の考え方を組み込む手法が研究されています。Scaramuzzaらの研究では、非線形MPCにオンライン学習機構を統合し、モデルの不確かさを逐次推定して補正する**適応型NMPC**を提案しています​
    
    [researchgate.net](https://www.researchgate.net/publication/382288247_MRS_ArduPilot_An_Adaptive_ArduPilot_Architecture_Based_on_Model_Reference_Stabilization#:~:text=revolutionize%20shipping%2C%20transportation%2C%20and%20search,proposed%20architecture%20generalizes%20to%20many)
    
    。その結果、風やペイロード変化といった大きな摂動下でも非適応型に比べ90%以上追従誤差を減少させ、さらにレーシングドローンのような高ダイナミクス飛行でも同一の制御器で安定飛行が可能となったと報告されています​
    
    [researchgate.net](https://www.researchgate.net/publication/382288247_MRS_ArduPilot_An_Adaptive_ArduPilot_Architecture_Based_on_Model_Reference_Stabilization#:~:text=adaptive%20NMPC%20to%20learn%20model,70%20km%2Fh%2C%20offering%20tracking%20performance)
    
    。他にも、ロバストMPCでモデル誤差に対する保証を与えたり、CBFを用いて外乱下でも安全集合から逸脱しない補助制御（**安全フィルタ**）を掛けるといった手法も有効です。実際、前述のPX4-CBFフィルタの研究では、視野が限定されたセンサ環境下でも追加の制約をCBFに組み込むことで安全性を維持しています​
    
    [github.com](https://github.com/ntnu-arl/PX4-CBF#:~:text=When%20using%20a%20laterally%20constrained,resources%20on%20the%20controller%20board)
    
    。このように、計算負荷の低減、遅延への対処、モデル不確かさへの適応といった技術的工夫により、MPC・CBFの実機適用上の課題を克服する研究が進んでいます。
    

# 高レベル・低レベル制御の階層的アーキテクチャ

ドローンの制御系設計では、高度な制御アルゴリズムを直接全ての軸に適用するのではなく、**高レベル（外部）制御**と**低レベル（内部）制御**に機能を分けた階層型アーキテクチャを採用する例が多く見られます​

[kth.diva-portal.org](https://kth.diva-portal.org/smash/get/diva2:1479331/FULLTEXT01.pdf#:~:text=More%20recently%2C%20in%202014%20a,level)

。典型的には、低レベルでは機体の姿勢や角速度を高速に安定化させ（PIDやLQRなどによるモーター・姿勢制御ループ）、高レベルでは位置や経路の追従を司るようにします。研究事例として、ある2014年の研究では**低レベルをモーター速度制御と姿勢制御のループ、高レベルをMPCによる軌道追従制御**に分離し、オンボードでリアルタイム実行することでクアッドロータの自律飛行を実現しています​

[kth.diva-portal.org](https://kth.diva-portal.org/smash/get/diva2:1479331/FULLTEXT01.pdf#:~:text=More%20recently%2C%20in%202014%20a,level)

。このような階層構造により、高レベルでは最適経路追従や衝突回避といった複雑な計算を行いつつ、低レベルでは高速応答が要求される姿勢安定化を専任させることができます。さらに発展的な例として、ドイツ航空宇宙センター(DLR)の研究では**二層のMPC制御**を用いています。一段目（高レベル）は移動地形や障害物を考慮した移動経路を計画する線形離散化モデルのMPCプランナー、二段目（低レベル）は機体の詳細な非線形モデルに基づき外乱にロバストなチューブMPCで追従制御を行う構成です​

[elib.dlr.de](https://elib.dlr.de/195608/1/Koegel%20-%20Safe%20hierarchical%20model%20predictive%20control%20and%20planning%20for%20autonomous%20systems.pdf#:~:text=problem%20setup,use%20rem%20to%20denote%20the)

​

[elib.dlr.de](https://elib.dlr.de/195608/1/Koegel%20-%20Safe%20hierarchical%20model%20predictive%20control%20and%20planning%20for%20autonomous%20systems.pdf#:~:text=moving%20horizon%20planning%20problem,remainder%20function%20of%20the%20Euclidean)

。高レベルプランナーが緩やかな時間スケール（例：数百ms単位）でリファレンス軌道を生成し、低レベルMPCがそれを高速サンプリング（例：数十ms以下）で追従・微修正することで、計算負荷を分散しつつ安全性と最適性を確保しています。この階層MPC間では**“契約”**と呼ばれる考え方で整合性を保証し、上位の計画軌道からのずれを下位制御が吸収できる範囲に抑えることで、理論的な安定性保証も図られています​

[elib.dlr.de](https://elib.dlr.de/195608/1/Koegel%20-%20Safe%20hierarchical%20model%20predictive%20control%20and%20planning%20for%20autonomous%20systems.pdf#:~:text=conjunction%20with%20the%20planning%20layer%2C,Section%203%20outlines)

​

[elib.dlr.de](https://elib.dlr.de/195608/1/Koegel%20-%20Safe%20hierarchical%20model%20predictive%20control%20and%20planning%20for%20autonomous%20systems.pdf#:~:text=problem%20setup,use%20rem%20to%20denote%20the)

。以上のように、高位の計画・最適制御と低位の安定化制御を分担させるアプローチは、多くの研究で採用される有効な設計手法であり、MPCやCBFを実用的な形でドローンに適用する鍵となっています。

# 多項式軌道表現とMPC・LQRの統合手法

ドローンの軌道計画と制御では、**多項式による軌道表現**と古典的な最適制御（LQR）やMPCを統合する手法も研究されています。代表的なのが**差分フラット性**を利用した多項式軌道生成で、MellingerとKumarによる2011年の研究はクアッドロータの軌道を滑らかな多項式スプラインで表現し、スプライン係数を最適化することで**最小スナップ軌道**をリアルタイムに生成するアルゴリズムを確立しました​

ras.papercept.net

。この手法では、生成された軌道自体が滑らかで実行可能な速度・加速度プロファイルを持つため、あとは機体がその軌道を追従できるよう制御器を設計するだけでよく、当初の研究ではPD制御に前馈補償を加えて軌道追従を実現しました（後にはLQRによる安定化も導入）。実際、近年の研究では**誤差状態LQR**と呼ばれる手法で多項式軌道追従を高精度化する試みもなされています。これは、軌道からの偏差（誤差状態）を状態変数とすることでシステムを線形近似し、その誤差ダイナミクスにLQRを適用するものです。Torgesenによる研究ではパロット社の小型ドローンに対し、生成した位置・速度・加速度・ジャーク軌道を追従するLQR制御を実装し、従来のPID制御よりも高い精度で連続軌道の追従が可能であることを示しています​

[andrewtorgesen.github.io](https://andrewtorgesen.github.io/res/16.31%20Final%20Project%20PAPER.pdf#:~:text=multirotor%20dynamics%2C%20is%20able%20to,the%20augmented%20flight%20control%20system)

。一方で、**多項式軌道とMPCの融合**も注目されています。軌道生成と追従制御を分離するのではなく、MPCの最適化問題に多項式軌道のパラメータを直接含めて解く手法です。ある研究例では、参考軌道やシステム出力を**ベジエ曲線（多項式スプライン）で表現**し、MPCの最適化変数とすることで問題を標準的な二次計画問題(QP)に落とし込み、さらにそれを多_parametric QPとして離線ソルバで解くことで**解析的なMPC解**を得ることに成功しています​

[kth.diva-portal.org](https://kth.diva-portal.org/smash/get/diva2:1479331/FULLTEXT01.pdf#:~:text=so%02lution%20of%20model%20predictive%20control,22)

。このアプローチでは、軌道の時間パラメータ化をBezier多項式で行うことで最適化の次元を削減し、得られた解は状態フィードバック則としてオンラインで即時に実行可能となります​

[kth.diva-portal.org](https://kth.diva-portal.org/smash/get/diva2:1479331/FULLTEXT01.pdf#:~:text=has%20been%20proposed,22)

。結果として、従来のように時間パラメータ付きの軌道を事前計算してから追従制御するのではなく、**軌道計画と制御を一体化**した最適制御が実現でき、計算効率と性能の両立が図られています。さらに最近では、従来の最小スナップ軌道を時間最適に改良する**モデル予測輪郭制御（MPCC）**の手法も提案されており、任意の連続空間曲線を与えるとMPCがオンラインで最適なタイミングで通過するよう制御することで、事前に時間パラメータ化した軌道追従より高速な飛行が可能になることが報告されています​

[rpg.ifi.uzh.ch](https://rpg.ifi.uzh.ch/docs/TRO22_MPCC_Romero.pdf#:~:text=using%20a%20simpler%20point,RELATED%20WORK)

​

[rpg.ifi.uzh.ch](https://rpg.ifi.uzh.ch/docs/TRO22_MPCC_Romero.pdf#:~:text=We%20show%20that%20the%20proposed,RELATED%20WORK)

。このように、多項式による軌道表現の長所（可算性・滑らかさ）とMPC/LQRなど制御手法の長所（制約処理やロバスト安定性）を組み合わせる研究が進んでおり、ドローンの高精度かつ高応答な飛行制御に寄与しています。

**参考文献**（主要な学術会議・ジャーナルから）：Mellinger and Kumar (ICRA 2011)、Romero _et al._ (T-RO 2022)​

[rpg.ifi.uzh.ch](https://rpg.ifi.uzh.ch/docs/TRO22_MPCC_Romero.pdf#:~:text=Nonlinear%20controllers%20have%20been%20proposed,principle%20models%20%5B27%5D%2C%20Gaussian%02process%20models)

​

[rpg.ifi.uzh.ch](https://rpg.ifi.uzh.ch/docs/TRO22_MPCC_Romero.pdf#:~:text=using%20a%20simpler%20point,RELATED%20WORK)

、Hanover _et al._ (RA-L 2021)​

[researchgate.net](https://www.researchgate.net/publication/382288247_MRS_ArduPilot_An_Adaptive_ArduPilot_Architecture_Based_on_Model_Reference_Stabilization#:~:text=revolutionize%20shipping%2C%20transportation%2C%20and%20search,proposed%20architecture%20generalizes%20to%20many)

、Baldi _et al._ (Control Eng. Practice 2022)​

[researchgate.net](https://www.researchgate.net/publication/382288247_MRS_ArduPilot_An_Adaptive_ArduPilot_Architecture_Based_on_Model_Reference_Stabilization#:~:text=This%20article%20presents%20an%20adaptive,attitude%20and%20total%20energy%20control)

、Do and Prodan (arXiv 2023)​

[arxiv.org](https://arxiv.org/abs/2308.15946#:~:text=,quadcopter%20position%20stabilization%20by%20analyzing)

、Agrawal and Sreenath (RSS 2017)​

[roboticsproceedings.org](https://roboticsproceedings.org/rss13/p73.pdf#:~:text=gained%20success%20in%20a%20wide,maintains%20the%20states%20of%20the)

、Tayal _et al._ (ICRA 2023)​

[arxiv.org](https://arxiv.org/pdf/2303.15871#:~:text=is%20a%20model,NMPC%2C%20on%20the%20other%20hand)

、ほか多数。