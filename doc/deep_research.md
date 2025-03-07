**1. Absence of an exact match:** No single prior work was found that fully integrates a **collaborative multi-UAV visual-inertial SLAM system with active perception (feature co-visibility planning) and a safety-critical control law (e.g. CBF)**. Existing research addresses these aspects separately – e.g. multi-UAV SLAM frameworks, cooperative active perception strategies, and safety-critical control – but none combines all into one unified approach.

**2. Related research (≥20 works) and novelty context:** We identify key related studies in three areas, highlighting how the proposed theme differs from each:

- **Multi-UAV Collaborative SLAM/VIO:** _COVINS_ is a centralized collaborative visual-inertial SLAM system where each UAV runs onboard VIO and a server merges maps via inter-agent loop closures​
    
    [arxiv.org](https://arxiv.org/abs/2108.05756#:~:text=,or%20a%20remote%20cloud%20server)
    
    ​
    
    [arxiv.org](https://arxiv.org/abs/2108.05756#:~:text=The%20server%20back,12%20agents%20jointly%20performing%20SLAM)
    
    . This improves multi-UAV pose accuracy but assumes passive data collection (no active viewpoint planning). _COVINS-G_ generalizes the back-end to work with arbitrary VIO front-ends and purely image-based loop-closure detection​
    
    [arxiv.org](https://arxiv.org/abs/2301.07147#:~:text=reference%20frame%2C%20which%20is%20of,enabling%20the%20compatibility%20of%20the)
    
    ​
    
    [arxiv.org](https://arxiv.org/abs/2301.07147#:~:text=server,end)
    
    , boosting flexibility but again not addressing how agents should move. _Kimera-Multi_ (Carlone et al.) achieves fully **distributed** multi-robot VIO SLAM with robust inter-robot loop closure and even builds a shared metric-semantic map​
    
    [arxiv.org](https://arxiv.org/abs/2011.04087#:~:text=,maximum%20clique%20outlier%20rejection%3B%20the)
    
    . However, like other SLAM back-ends, these assume agents explore or operate on pre-planned paths – **they do not actively coordinate trajectories for better mapping**. The novelty of the proposed work is to add an _active perception layer_ on top of such SLAM frameworks, so that UAVs plan motions to gain overlapping fields of view and feature matches, rather than relying on chance encounters for loop closures.
    
- **Cooperative Active Perception & SLAM:** Many works have studied robots actively controlling their motion to improve perception or mapping. For example, Atanasov _et al._ (2015) developed a **decentralized active information acquisition** approach for multi-robot SLAM​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,agent%20information%02theoretic%20control%20for%20target)
    
    , formulating control policies that reduce estimation uncertainty. Chen _et al._ (RA-L 2020) propose a **“cooperative active pose-graph SLAM”** where multiple robots identify weak areas in the SLAM pose graph and plan trajectories to obtain new loop-closure measurements​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/143814/2/Binder2.pdf#:~:text=on%20graph%20topology,SLAM%2C%20in%20terms%20of%20information)
    
    . Their method uses submodular optimization to select actions that strengthen inter-robot map connections, and they demonstrated uncertainty reduction with two UAVs​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/143814/2/Binder2.pdf#:~:text=the%20selected%20measurements%20through%20a,UAVs)
    
    . These studies show robots can coordinate to improve SLAM; however, their planning objective is information-theoretic (e.g. Fisher info or entropy) rather than explicitly **ensuring shared field-of-view for feature matching**. The proposed research is novel in focusing on _feature co-visibility_: planning UAV viewpoints so they see common features (maximizing FOV intersection) to facilitate **collaborative VIO** – an aspect only implicit in prior info-theoretic methods.
    
- **Active Target Tracking and Localization:** Cooperative active perception has also been explored in multi-UAV target tracking. Jacquet _et al._ (RA-L 2022) designed a nonlinear MPC that drives multiple drones to minimize the uncertainty of a moving target’s pose, using a **cooperative Kalman filter** in the loop​
    
    [lausr.org](https://lausr.org/dashboard/?doi=10.1109/lra.2022.3143218#:~:text=This%20letter%20introduces%20a%20cooperative,framework%20allows%20and%20exploits%20heterogeneity)
    
    . Their controller incorporates the real drone dynamics and sensor FOV constraints, leading the team to optimal sensing configurations​
    
    [lausr.org](https://lausr.org/dashboard/?doi=10.1109/lra.2022.3143218#:~:text=moving%20feature%20which%20is%20observed,to%20reduce%20the%20cooperative%20estimation)
    
    . Bourne _et al._ (IJRR 2020) developed a decentralized multi-UAV control strategy for **actively localizing a gas leak**, using Bayesian estimators and informative path planning with collision avoidance​
    
    [colab.ws](https://colab.ws/articles/10.1177/0278364920957090#:~:text=This%20article%20presents%20a%20new,gain)
    
    . These works actively control UAVs for perception, but they assume a single known target or feature. In contrast, the proposed theme addresses **SLAM with many features**: planning for general map points and inter-UAV loop closures, which is more complex. Furthermore, our integration of a formal safety mechanism (CBF) into the active SLAM loop is novel – past approaches like Jacquet’s NMPC enforce sensing configurations but do not guarantee collision avoidance or field-of-view maintenance through provable constraints (they rely on tuned cost terms).
    
- **Active Vision in UAV Swarms:** Related to feature co-visibility, Zhang _et al._ (RA-L 2022) tackled the limited camera FOV in drone swarms by introducing **distributed active vision-based relative localization**. Each drone dynamically adjusts its viewpoint (via gimbal or motion) to keep neighbors in sight, guided by a graph-based attention planner​
    
    [arxiv.org](https://arxiv.org/pdf/2108.05505#:~:text=Abstract%E2%80%94%20The%20vision,results%20are%20fused%20with%20onboard)
    
    . Fusing these active observations improved formation control accuracy​
    
    [arxiv.org](https://arxiv.org/pdf/2108.05505#:~:text=with%20this%20issue%2C%20this%20letter,formation%20control%20performance%20of%20the)
    
    . This demonstrates active control of cameras to maintain mutual visibility, akin to our idea of maintaining common FOV for landmarks. However, Zhang’s focus is on **relative localization for formation** (each drone tracks others), not building a global map of the environment. Our work extends active vision principles to **SLAM targets (environment features)** and multiple agents, requiring different planning criteria (e.g. where to explore for new features vs. when to rendezvous for map merging).
    
- **Perception-Constrained Optimal Control:** A few works have explicitly integrated perception objectives or constraints into UAV control design. Falanga _et al._ (IROS 2018) presented **PAMPC**, an MPC that jointly optimizes control performance and perception quality​
    
    [arxiv.org](https://arxiv.org/pdf/1804.04811#:~:text=Abstract%E2%80%94%20We%20present%20the%20first,Considering%20both)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/1804.04811#:~:text=optimizes%20perception%20objectives%20for%20robust,require%20to%20minimize%20such%20rotation)
    
    . For example, it plans quadrotor motions that keep a point-of-interest in view (minimizing image velocity) while respecting dynamics. This **unifies planning and vision**, but in a single-UAV context and without map-sharing between agents. The proposed research will similarly unify control and perception, but for **multi-UAV SLAM** and with formal safety guarantees. The novelty lies in using **Control Barrier Functions (CBFs)** to enforce perception constraints _and_ safety in real time. For instance, a CBF could maintain that a landmark or a teammate remains in a UAV’s camera FOV (a “visibility safety set”), while also preventing inter-UAV collisions – something not addressed in perception-aware MPC literature.
    
- **Safety-Critical Control (CBF) for Vision-Based Tasks:** Recent works show the potential of CBFs to handle vision-related constraints. Zheng _et al._ (T-Mech 2019) used a CBF-based controller to guarantee a quadrotor’s onboard camera keeps a fixed marker in view during flight, effectively **ensuring visibility** as the UAV moves​
    
    [arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=issue%20is%20also%20addressed%2C%20for,to%20their%20larger%20cost%20and)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=second%20proposes%20a%20Control%20Barrier,to%20their%20larger%20cost%20and)
    
    . Trimarchi _et al._ (2024) extend this idea by formulating a CBF that keeps features inside the FOV without knowing exact range – their method guarantees FOV constraints despite unknown distances, demonstrated by a drone keeping a racing gate in sight​
    
    [arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=Abstract%E2%80%94%20The%20problem%20of%20control,approach%20that%20uses%20a%20splitting)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=dependence%20on%20the%20unknown%20measurement,the%20camera%20field%20of%20view)
    
    . These efforts are **single-robot** and focus on one target or static features. Our proposed work is novel in applying CBFs in a _multi-robot_ setting: we aim to maintain **mutual visibility or common landmark observations among multiple UAVs**. This involves multiple coupled field-of-view constraints and obstacle avoidance between robots, a scenario not directly covered by existing CBF applications (which typically handle one robot and a static obstacle or target).
    
- **Active Multi-robot Systems with Mixed Objectives:** Some prior studies consider _both_ safety and information gain, but in simpler forms. For example, Bourne’s gas-leak localization included a collision avoidance controller​
    
    [colab.ws](https://colab.ws/articles/10.1177/0278364920957090#:~:text=The%20algorithm%20consists%20of%3A%20,Extensive%20simulations%20are)
    
    , and Chen’s 2020 framework allowed other tasks during active SLAM​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/143814/2/Binder2.pdf#:~:text=We%20are%20interested%20in%20cooperative,2019%3B%20Accepted%20January%2C%2020%2C%202020)
    
    ​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/143814/2/Binder2.pdf#:~:text=active%20SLAM%20framework%20that%20requires,to%20choose%20the%20best%20future)
    
    . However, these did not use formal CBF theory for safety; the proposed integration of optimal estimation, active exploration, and CBF-based safety is unprecedented. **In summary, no existing work simultaneously optimizes multi-UAV SLAM accuracy (via active co-visibility planning) and guarantees safety (via CBF constraints)**. The novelty is the synergy: using CBFs to keep agents and key landmarks within “sensing range” of each other (preventing loss of visual contact) and to avoid collisions, while an active-SLAM planner selects trajectories that maximally reduce pose uncertainty or map error.
    

**3. References (selected):**

- Patrik Schmuck _et al._, “**COVINS: Visual-Inertial SLAM for Centralized Collaboration**,” _IEEE RA-L_, 2021 – Multi-UAV SLAM system with a centralized backend fusing visual-inertial odometry from >10 agents​
    
    [arxiv.org](https://arxiv.org/abs/2108.05756#:~:text=,or%20a%20remote%20cloud%20server)
    
    ​
    
    [arxiv.org](https://arxiv.org/abs/2108.05756#:~:text=The%20server%20back,12%20agents%20jointly%20performing%20SLAM)
    
    .
    
- Manthan Patel _et al._, “**COVINS-G: A Generic Back-end for Collaborative VINS**,” _ICRA 2023_ – Extends COVINS with a backend compatible with any VIO front-end and image-only loop closures​
    
    [arxiv.org](https://arxiv.org/abs/2301.07147#:~:text=reference%20frame%2C%20which%20is%20of,enabling%20the%20compatibility%20of%20the)
    
    ​
    
    [arxiv.org](https://arxiv.org/abs/2301.07147#:~:text=server,end)
    
    .
    
- Yun Chang _et al._, “**Kimera-Multi: Distributed Multi-Robot Metric-Semantic SLAM**,” _ICRA 2021_ – Fully distributed multi-robot VIO SLAM, with each robot running VIO and sharing loop closures for joint pose graph optimization​
    
    [arxiv.org](https://arxiv.org/abs/2011.04087#:~:text=,maximum%20clique%20outlier%20rejection%3B%20the)
    
    .
    
- Mitch Bryson and Salah Sukkarieh, “**Architectures for Cooperative Airborne SLAM**,” _J. Intell. Robotic Syst._, 2009 – Early work on multiple UAVs performing vision-based SLAM cooperatively, establishing fundamental system architecture​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,Luca%20Carlone%2C%20Jingjing%20Du)
    
    .
    
- Yongbo Chen _et al._, “**Broadcast Your Weaknesses: Cooperative Active Pose-Graph SLAM**,” _IEEE RA-L_, 2020 – Robots share “weak” SLAM loop closures and plan paths to fix them (information-driven multi-robot active SLAM), demonstrated with UAVs​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/143814/2/Binder2.pdf#:~:text=on%20graph%20topology,SLAM%2C%20in%20terms%20of%20information)
    
    ​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/143814/2/Binder2.pdf#:~:text=the%20selected%20measurements%20through%20a,UAVs)
    
    .
    
- Martin Jacquet _et al._, “**Motor-Level NMPC for Cooperative Active Perception (Multi-UAV)**,” _IEEE RA-L_, 2022 – Multi-drone nonlinear MPC that accounts for estimator uncertainty, driving drones to optimal viewpoints for tracking a moving feature​
    
    [lausr.org](https://lausr.org/dashboard/?doi=10.1109/lra.2022.3143218#:~:text=This%20letter%20introduces%20a%20cooperative,framework%20allows%20and%20exploits%20heterogeneity)
    
    ​
    
    [lausr.org](https://lausr.org/dashboard/?doi=10.1109/lra.2022.3143218#:~:text=moving%20feature%20which%20is%20observed,to%20reduce%20the%20cooperative%20estimation)
    
    .
    
- Peihan Zhang _et al._, “**Active Vision–Based Relative Localization for Aerial Swarms**,” _IEEE RA-L_, 2022 – Drones actively orient cameras to keep neighbors in view, overcoming limited FOV and improving swarm formation accuracy​
    
    [arxiv.org](https://arxiv.org/pdf/2108.05505#:~:text=Abstract%E2%80%94%20The%20vision,results%20are%20fused%20with%20onboard)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/2108.05505#:~:text=with%20this%20issue%2C%20this%20letter,formation%20control%20performance%20of%20the)
    
    .
    
- Davide Falanga _et al._, “**PAMPC: Perception-Aware MPC for Quadrotors**,” _IROS 2018_ – UAV trajectory optimization that balances control objectives with perception (e.g. maintaining visibility of a point of interest)​
    
    [arxiv.org](https://arxiv.org/pdf/1804.04811#:~:text=Abstract%E2%80%94%20We%20present%20the%20first,Considering%20both)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/1804.04811#:~:text=optimizes%20perception%20objectives%20for%20robust,require%20to%20minimize%20such%20rotation)
    
    .
    
- D. Zheng _et al._, “**Toward Visibility-Guaranteed Visual Servoing of Quadrotors**,” _IEEE/ASME T-Mech._, 2019 – Introduces a CBF-based controller that keeps a visual fiducial marker in the drone’s camera FOV at all times, ensuring continuous localization​
    
    [arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=issue%20is%20also%20addressed%2C%20for,to%20their%20larger%20cost%20and)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=second%20proposes%20a%20Control%20Barrier,to%20their%20larger%20cost%20and)
    
    .
    
- Biagio Trimarchi _et al._, “**A CBF Candidate for Limited FOV Sensors**,” _arXiv e-Print_, 2024 – Proposes a novel CBF approach for vision-based control that guarantees camera FOV constraints _without_ knowing exact feature distance, demonstrated with a drone keeping a gate in view​
    
    [arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=Abstract%E2%80%94%20The%20problem%20of%20control,approach%20that%20uses%20a%20splitting)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=dependence%20on%20the%20unknown%20measurement,the%20camera%20field%20of%20view)
    
    .
    
- Nikolay Atanasov _et al._, “**Decentralized Active Information Acquisition for Multi-Robot SLAM**,” _ICRA 2015_ – Theoretical framework for multi-robot control that maximizes information gain for SLAM, a precursor to modern active SLAM methods​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,agent%20information%02theoretic%20control%20for%20target)
    
    .
    
- Joseph R. Bourne _et al._, “**Decentralized Multi-Agent Info-Theoretic Control for Target Localization: Gas Leaks**,” _IJRR_, 2020 – Multi-UAV Bayesian search planning for a gas leak, with an information-driven trajectory planner and collision avoidance for safety​
    
    [colab.ws](https://colab.ws/articles/10.1177/0278364920957090#:~:text=This%20article%20presents%20a%20new,gain)
    
    .
    
- Benjamin Charrow _et al._, “**Information-Theoretic Planning with Trajectory Optimization for Dense 3D Mapping**,” _RSS 2015_ – Uses trajectory optimization (Cauchy-Schwarz quadratic mutual information) to guide a robot and build a dense map, an example of single-robot active SLAM​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,Science%20and%20Systems%20XI%2C%202015)
    
    .
    
- Henry Carrillo _et al._, “**On the Comparison of Uncertainty Criteria for Active SLAM**,” _ICRA 2012_ – Analyzes different information metrics (e.g. entropy, D-optimal) for planning SLAM trajectories, highlighting the trade-offs in active SLAM objective choices​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,Robotics%3A%20Science)
    
    .
    
- Luca Carlone _et al._, “**Active SLAM via Kullback–Leibler Divergence**,” _IROS 2010_ – Early active SLAM approach using KL-divergence to select viewpoints that reduce localization uncertainty​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,on%20Robotics%20and%20Automation%2C%20pages)
    
    .
    
- Yiannis Kantaros _et al._, “**Asymptotically Optimal Planning for Non-Myopic Multi-Robot Info Gathering**,” _Robotics: Science & Systems 2019_ – Develops algorithms for teams of robots to plan long-horizon trajectories maximizing information gain (extends active perception to multi-step, multi-robot scenarios)​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,Science%20and%20Systems%20XV%2C%202019)
    
    .
    
- Yiannis Kantaros and George J. Pappas, “**Scalable Active Information Acquisition for Multi-Robot Systems**,” _ICRA 2021_ – Addresses the computational complexity of multi-robot active information gathering, proposing scalable strategies (relevant to extending active SLAM to larger teams)​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,Conference%20on%20Robotics%20and%20Automation)
    
    .
    
- Yongbo Chen _et al._, “**Active SLAM with Area Coverage and Obstacle Avoidance**,” _IEEE/ASME T-Mech._, 2020 – Active SLAM on a single robot integrating exploration (coverage) and safety (obstacle avoidance), showing the benefit of combining mapping objectives with safety constraints​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,IEEE%20Robotics%20and%20Automation)
    
    .
    
- Mitch Bryson and Salah Sukkarieh, “**Co-operative Localization and Mapping for Multiple UAVs**,” _IEEE Aero. Conf. 2007_ – One of the first demonstrations of two UAVs sharing visual SLAM information in real time, establishing feasibility of collaborative SLAM in unknown environments​
    
    [opus.lib.uts.edu.au](https://opus.lib.uts.edu.au/bitstream/10453/170038/2/Multi-robot%20Active%20SLAM%20based%20on%20Submap-joining%20for%20Feature-based%20Representation%20Environments.pdf#:~:text=,Luca%20Carlone%2C%20Jingjing%20Du)
    
    .
    
- **(Survey)** Amir Ahmad _et al._, “**Active SLAM: A Review of the Last Decade**,” _Sensors_, 2021 – Comprehensive survey of active SLAM techniques, noting that while methods have improved mapping efficiency, challenges remain in multi-robot coordination and in balancing exploration vs. safety​
    
    [mdpi.com](https://www.mdpi.com/1424-8220/23/19/8097#:~:text=This%20article%20presents%20a%20comprehensive,TOED)
    
    ​
    
    [arxiv.org](https://arxiv.org/abs/2207.00254#:~:text=,attention%20across%20different%20scientific%20communities)
    
    . (Provides context and confirms no prior work has unified active SLAM with formal safety constraints in multi-UAV settings.)
    

Overall, these works address pieces of the puzzle. **Our approach’s novelty** is in unifying them: a multi-UAV SLAM system where agents actively plan **joint viewpoints** (ensuring feature overlap for collaborative mapping) and simultaneously enforce **safety/visibility constraints via CBF**, which has not been done in prior research​

[arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=issue%20is%20also%20addressed%2C%20for,to%20their%20larger%20cost%20and)

​

[arxiv.org](https://arxiv.org/pdf/2410.01277#:~:text=dependence%20on%20the%20unknown%20measurement,the%20camera%20field%20of%20view)

. This integration will enable a team of UAVs to map and localize more accurately than passive SLAM alone​

[arxiv.org](https://arxiv.org/abs/2108.05756#:~:text=The%20server%20back,12%20agents%20jointly%20performing%20SLAM)

, while rigorously maintaining safety and continuous mutual observations – a combination of capabilities unique to our proposed study. Each reference above either lacks the multi-agent active coordination, or the safety-critical control, or the SLAM-specific visual focus, whereas our work innovates by bringing all these together.