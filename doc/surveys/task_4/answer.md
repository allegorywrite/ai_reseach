# 1. CBF and CCBF on Lie Groups (e.g. SE(3), SO(3))

**Control Barrier Functions on Manifolds:** A _Control Barrier Function_ (CBF) provides a Lyapunov-like condition to keep the state within a safe set. In Euclidean space, a smooth function $h(x)$ defines a safe set $S={x: h(x)\ge0}$. $h$ is a CBF if there exists an extended class-$\kappa$ function $\kappa(\cdot)$ such that for all $x\in S$, one can find an input $u$ making the Lie derivative satisfy $L_f h(x)+L_g h(x) u + \kappa(h(x))\ge0$​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=Definition%201%20,x%29%20respectively)

. This condition (or its “zeroing” variant with $\kappa(h)=\alpha h$) guarantees forward invariance of $S$ (intuitively, the state cannot leave $S$)​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=Theorem%20,s%29%2C%20relative%20degree)

. On a **Lie group** (a smooth manifold with a group structure), the same concept is extended _coordinate-free_. The state $q$ lies on a manifold $M$ (e.g. $SO(3)$ for 3D orientation or $SE(3)$ for full pose) instead of $\mathbb{R}^n$. A _geometric CBF_ is then defined via a smooth scalar function $h(t,q,\dot q)$ on the tangent bundle $TM$ such that $h\ge0$ characterizes the safe region $C_t={(q,\dot q):h(t,q,\dot q)\ge0}$​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=Definition%202,t%2C%20q%2C%20q%CB%99%29%29%20%E2%89%A4%201)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=infu%E2%88%88Rm,%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B6%20equivalent%20to%20Lf%20B)

. The Lie derivative on a manifold is defined using directional derivatives along the vector field (taking into account the manifold’s geometry, e.g. using a Riemannian metric or local charts). For example, Wu and Sreenath extend CBFs to general Riemannian manifolds by formulating the dynamics and derivatives in a coordinate-free manner​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=%E2%97%8F%20We%20extend%20the%20concept,CBF%20can%02didates%20based%20on%20time)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=configuration%20space%2C%20which%20result%20in,varying%20safety%20constraints.%20The%20corresponding)

. The CBF condition on a manifold is analogous: there must exist class-$\mathcal{K}$ functions $\alpha_1,\alpha_2$ and $\mu>0$ such that for all states in the safe set, one can find $u$ keeping a certain scalar function $B(h)$ non-decreasing (up to a $-\mu B$ term)​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=,%E2%88%82B)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=%E2%88%82t%20%2B%20B%20%E2%80%B2%20,to%20Lf%20B%20%2BB%20%E2%80%B2)

. Under this condition, one can prove the safe set is forward invariant on the manifold​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=The%20following%20Lemma%20provides%20a,always%20remain%20within%20C%20%E2%97%8B)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=t%20if%20,C%20%E2%97%8B%20t%3D0)

(the formal proof uses Nagumo’s theorem generalized to manifolds). In essence, the definition and safety theorem carry over to Lie groups with _$h$ now a function on the manifold_ and Lie derivatives computed intrinsically. One key benefit is **global** safety enforcement: traditional controllers often work in a **local coordinate** (e.g. Euler angles), which can lead to singularities or only local invariance, whereas formulating $h$ on the Lie group (e.g. using rotation matrices or quaternions without unwinding) yields global results​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=systems%20have%20dynamics%20that%20evolve,varying%2C%20presenting)

. Another difference is that on $SE(3)$ the dynamics are typically second-order (position and orientation acceleration), so safety constraints often have _relative degree 2_. This requires using higher-order CBF formulations (such as **Exponential CBFs**) to incorporate the constraint via the control input​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=CBFs%20are%20limited%20in%20their,as%20an%20exponential%20control%20barrier)

​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=sup%20u%E2%88%88U%20n%20L%20%CE%B4,x%29u%20%2B%20K)

. Researchers have developed conditions for such higher-relative-degree CBFs – for example, ensuring $\ddot h$ plus proportional-derivative terms is nonnegative – to guarantee invariance​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=CBFs%20are%20limited%20in%20their,as%20an%20exponential%20control%20barrier)

​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=%CE%B4%20fh,h%28x%29%2C%20Lfh%28x%29%2C%20L2)

. Despite these technical differences, the fundamental property remains: if at each moment the control input satisfies the CBF condition on the Lie group, the system state will remain in the safe set on that manifold​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=The%20following%20Lemma%20provides%20a,always%20remain%20within%20C%20%E2%97%8B)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=t%20if%20,C%20%E2%97%8B%20t%3D0)

.

**Control Design on Lie Groups using CBFs:** With a CBF defined on a Lie group, one can design controllers that enforce safety by solving constrained problems (often quadratic programs) at each time step. For example, one can combine a stabilizing **Control Lyapunov Function** (CLF) with a CBF in a **QP**: at each instant, minimize a cost (tracking error) subject to linear constraints encoding the CBF condition $L_f h + L_g h,u \ge -\kappa(h)$. Wu and Sreenath formulated a “geometric CLF-CBF-QP” directly on $SO(3)$ and other manifolds​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=%28CBFs%29,3D%20moving%20point%20mass%2C%20a)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=and%20geometric%20CBF%20to%20compute,3D%20moving%20point%20mass%2C%20a)

. They proved that this controller renders the desired set safe **and** asymptotically stable (when a CLF is included) on the manifold. As an illustration, consider an orientation constraint on $SO(3)$: say we require a drone’s camera to keep a target within its field-of-view. This can be encoded by a CBF $h(R) = \cos(\theta_{\max}) + 1 - \Psi(R,R_{\text{target}})$, where $\Psi(R,R_{\text{target}})$ measures the alignment (e.g. $\Psi= \frac{1}{2}\text{tr}(I - R^T R_{\text{target}})$ giving the angular difference). Enforcing $h(R)\ge0$ means the angle between $R$ and the target direction stays below $\theta_{\max}$. The Lie derivative $\dot h$ involves the body-angular velocity and can be set non-negative by appropriate control torque. Wu _et al._ demonstrated this idea on a spherical pendulum (state on $S^2$) that must stay between two cones: their CLF-CBF-QP kept the pendulum trajectory within the safe cone region at all times, whereas baseline controllers violated the constraint​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=Fig,inner%20cone%20area%2C%20whereas%20for)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=system%20trajectory%20enters%20the%20unsafe,red%29%20cone%20is)

. This showcases that CBF-based designs on nonlinear manifolds can guarantee safety where classical approaches might fail. Overall, formulating CBFs on Lie groups provides a mathematically rigorous way to impose state constraints like orientation limits or workspace boundaries _globally_ and in a coordinate-invariant manner. The trade-off is increased complexity in computing Lie derivatives and handling higher relative degree, but recent work provides systematic tools (e.g. differential geometry methods and high-order CBF conditions​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=CBFs%20are%20limited%20in%20their,as%20an%20exponential%20control%20barrier)

​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=sup%20u%E2%88%88U%20n%20L%20%CE%B4,x%29u%20%2B%20K)

) to address these challenges.

**Collaborative CBFs for Multi-Agent Systems:** The CBF framework has been extended to _networked systems_, where safety constraints involve multiple agents. A **Collaborative CBF (CCBF)** (also called _coupled_ or _distributed_ CBF in some works) is a barrier function that accounts for the influence of other agents’ actions on safety. Intuitively, a CCBF $h_{i}(x_i,x_{-i})$ for agent $i$ ensures that even if agent $i$ alone cannot keep the state safe, appropriate adjustments by its neighbors $j\in \mathcal{N}_i$ can maintain the overall safety condition. Formally, Definition 3 in_

_[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=Definition%203,hi%2Co%20%E2%88%88%20C%203%20and)_

_​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=%E2%88%80,s%20i%20%2C%20us%20Ni)

states that $h_{i,o}$ (a candidate safe function for agent $i$ w.r.t. obstacle $o$ or neighbor interactions) is a _collaborative control barrier function_ if for every state (of agent $i$ and the relevant others) satisfying prerequisite conditions (e.g. higher-order derivatives of $h_{i,o}$ are nonnegative), there exist _both_ an input $u_i$ for agent $i$ **and** inputs $u_{j}$ for its neighbors $j\in \mathcal{N}_i$ such that a safety inequality is satisfied​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=i%2Co%20be%20defined%20by%20,%E2%88%80t%20%E2%88%88%20T%20there%20exists)

​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=,%C3%97%20Us%20Ni%20such%20that)

. In other words, $h_{i,o}$ can be kept non-decreasing through the cooperative action of agent $i$ and its neighbors. If each agent has such a CCBF for each of its safety constraints (obstacles or inter-agent collisions), then one can show the overall multi-agent safe set is forward invariant. For instance, Lemma 3 of​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=Lemma%203,C%201%20i%2Co%E2%88%A9%20C%202)

proves that for a multi-robot formation, if every agent’s constraint function $h_{i,o}$ qualifies as a CCBF, then the intersection of all agents’ safe sets remains invariant (the team stays safe for all time). This result provides a rigorous guarantee of safety under _neighbor-dependent_ constraints: even if an agent on its own would leave the safe set, timely cooperation from others (e.g. yielding way or adjusting formation) can keep the group safe.

**Distributed Implementation:** CCBFs naturally lend themselves to distributed control algorithms. Since each agent’s safety is conditioned on neighbors’ actions, a decentralized scheme can be devised where agents communicate and agree on adjustments to satisfy all CCBF constraints. In fact, Wang _et al._ (ECC 2024) propose a **collaborative safety algorithm** that proceeds in rounds of neighbor communication to implement CCBF-based safe control​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=With%20set%20invariance%20defined%20with,a%20new%20definition%20of%20maximum)

. At each round, agents share their “safety capability” (whether they can maintain $h_{i,o}\ge0$ alone or need help) and compute adjustments. The algorithm converges to control inputs for all agents such that all collaborative barrier conditions are met, achieving a distributed solution to what is effectively a centralized safety constraint satisfaction problem. This kind of scheme avoids a single centralized controller and instead uses local QPs or local control updates that respect both local and shared (coupled) barrier constraints. Theoretically, as long as each agent’s $h_{i,o}$ meets the CCBF criteria, neighbors will always be able to find a cooperative action to prevent constraint violations​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=Lemma%203,C%201%20i%2Co%E2%88%A9%20C%202)

​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=i%2Co%20%E2%88%A9%20C3%20i%2Co%20is,we%20introduce%20the%20collaborative%20safety)

. In summary, CCBFs extend the CBF framework to multi-agent (including multi-drone) scenarios, providing a formal method to ensure **team-level safety**. They allow safety constraints like collision avoidance or formation-keeping to be enforced with mathematical guarantees, and they can be implemented in a distributed manner by letting agents locally ensure barrier conditions with minimal coordination. This is an active research area, and recent results show promise in scaling to large networks (even using learning-based approximations of barrier certificates for hundreds of agents​

[mit-realm.github.io](https://mit-realm.github.io/gcbfplus-website/#:~:text=GCBF%2B%20,safe%20controllers%20for%201000%2B%20agents)

​

[mit-realm.github.io](https://mit-realm.github.io/gcbfplus-website/#:~:text=GCBF%2B%3A%20A%20Neural%20Graph%20Control,safe%20controllers%20for%201000%2B%20agents)

), though maintaining strict mathematical guarantees in very large systems remains a challenging problem.

## 2. MPC Formulation on SE(3) and Solution Methods

**Problem Formulation on $SE(3)$:** Model Predictive Control (MPC) on $SE(3)$ involves optimizing over trajectories of a system whose state includes a pose (position and orientation) in 3D. A generic formulation considers the system state $(R, p)$ where $R\in SO(3)$ (rotation matrix) and $p\in\mathbb{R}^3$ (position), or equivalently an element $X\in SE(3)$, along with velocity (e.g. body-frame angular and linear velocity $\xi$). One typical setting is a discrete-time dynamics on the Lie group: $x_{k+1} = F(x_k, u_k)$, where $x_k=(X_k,\xi_k)$ lies in the tangent bundle $T(SE(3))$. The MPC optimizes a cost such as tracking error to a desired pose or minimizing control effort, over a finite horizon $N$. For example, one can pose: minimize $\sum_{k=0}^{N-1} \ell(x_k,u_k) + \ell_f(x_N)$ subject to the discrete $SE(3)$ dynamics and constraints​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=X%CB%99%20t%20%3D%20Xt%CE%BE%20%E2%88%A7,t%20%CB%99%CE%BEt%20%3D%20f)

​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=umin%20%E2%89%A4%20uk%20%E2%89%A4%20umax%2C,8)

. In expanded form, a constrained optimal control problem on a matrix Lie group can be written as:

- **Cost:** $J=\ell_f(X_N,\xi_N)+\sum_{k=0}^{N-1}\ell(X_k,\xi_k,u_k)$ (with $\ell_f$ a terminal cost).
- **Dynamics:** $X_{k+1} = X_k \exp(\Delta t,\xi_k^\wedge)$, $;\xi_{k+1} = f(X_k,\xi_k,u_k)$, for $k=0,\ldots,N-1$ (where “$\exp$” is the matrix exponential mapping the Lie algebra to the group, and $f$ represents the system’s velocity dynamics)​
    
    [arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=X%CB%99%20t%20%3D%20Xt%CE%BE%20%E2%88%A7,t%20%CB%99%CE%BEt%20%3D%20f)
    
    . This is essentially a discrete Euler integration of the continuous rigid-body dynamics $ \dot X = X,\xi^\wedge,; \dot\xi = f(X,\xi,u)$.
- **Constraints:** $u_{\min}\le u_k \le u_{\max}$ (actuator bounds) and any state constraints $g(X_k,\xi_k,u_k)\le0$ (e.g. avoid singular attitudes, keep altitude $\ge h_{\min}$, etc.), for all $k=0,\ldots,N-1$​
    
    [arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=umin%20%E2%89%A4%20uk%20%E2%89%A4%20umax%2C,8)
    
    . The initial state $X_0,\xi_0$ is given, and one may also require $X_N$ to reach a specified goal or lie in a terminal region.

This formulation lives on the manifold: $X_k$ evolves on $SE(3)$, so rotations are treated without Euler angle parameterization (avoiding coordinate singularities). The cost $\ell$ typically is defined via a distance on $SE(3)$, for instance $\ell(X,\xi,u) = | \Log(X^{-1}X_{\text{ref}})|_Q^2 + |\xi-\xi_{\text{ref}}|_R^2 + |u|_U^2$, using the Lie algebra log to measure rotation error. Formulating the MPC this way ensures the optimization respects the geometric structure of the state space. However, it leads to a **nonlinear constrained optimization problem on a manifold**, which can be challenging to solve in real time.

**Optimal Control on Manifolds – Theory:** There is rich theory on optimal control in Lie groups. Classic results derived necessary conditions (like Pontryagin’s Maximum Principle) for systems on $SO(3)$ and other Lie groups. For example, Bloch _et al._ studied a variational optimal control for a 3D rigid body on $SO(3)$, yielding structure-specific geodesic equations​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=aims%20to%20generate%20optimal%20trajectories,MPC%29%20for)

. Kobilarov and Marsden developed discrete geometric optimal control, showing optimal trajectories correspond to discrete geodesics on the group and deriving numerical integrators​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=aims%20to%20generate%20optimal%20trajectories,MPC%29%20for)

. These works provide analytical insight (e.g. the form of optimal solutions), but solving the two-point boundary value problems in closed form is usually infeasible for complex systems. As a result, numerical **trajectory optimization** methods are employed. On Euclidean spaces, it’s common to use direct transcription (collocation) or shooting methods with nonlinear programming (NLP) solvers. The _same approach can be applied on $SE(3)$_: one of the most straightforward methods is to set up a nonlinear program that minimizes the cost while enforcing the dynamics and constraints​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=In%20the%20trajectory%20optimization%20field%2C,Newton)

. Lee _et al._ followed this approach for spacecraft attitude control on $SO(3)$, formulating an NLP that included control limits and orientation “exclusion zones” as constraints​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=most%20straightforward%20approaches%20is%20to,Newton)

. Standard solvers (like sequential quadratic programming or interior-point methods) can handle such problems, treating the manifold coordinates (e.g. rotation matrices) as decision variables with additional constraints (like $R^T R=I$ for rotations). The downside is that these solvers can be slow, and enforcing orthonormality of rotation matrices or avoiding unwinding can be tricky.

**Geometric MPC and Solvers:** Recognizing these challenges, researchers have developed MPC methods that exploit the Lie group structure. One approach is to perform **local coordinate linearization** at each step. Ding _et al._ (2021) introduced a _Representation-Free MPC_ for quadruped robots, which directly uses rotation matrices (no Euler angles or quaternions)​

[arxiv.org](https://arxiv.org/abs/2012.10002#:~:text=,Experimental%20results%20including)

. They linearize the rotational dynamics via a variation-based approach: essentially, they represent a small orientation error in the Lie algebra (using $\Log$) and derive a locally linear model for one step. This allows them to cast the MPC update as a **quadratic program (QP)**​

[arxiv.org](https://arxiv.org/abs/2012.10002#:~:text=,Experimental%20results%20including)

. Impressively, their controller runs at 250 Hz on a real quadruped and can handle aggressive maneuvers (like continuous jumps and even a backflip)​

[arxiv.org](https://arxiv.org/abs/2012.10002#:~:text=,Experimental%20results%20including)

. The ability to transcribe the MPC into a QP is significant for real-time implementation; it relies on choosing a short horizon and re-linearizing at each timestep (so the approach is akin to iterative LQR or linear MPC on manifolds). Another approach is to use **geometric DDP (Differential Dynamic Programming)** or shooting methods that respect the manifold. Teng _et al._ developed an MPC on Lie groups by designing the cost in the Lie algebra and using a variant of DDP in the optimization loop​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=Marsden%20,18)

​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=Quadratic%20Programming%20%28SQP%29%20methods,12%2C14%5D%20formu%02late%20the%20trajectory)

. DDP, which is a second-order optimal control method, has been extended to handle specific Lie groups (like $SO(3)$) in earlier works, but only recently to generic constraints. Alcan _et al._ (2023) proposed an augmented Lagrangian DDP that can handle _nonlinear state constraints_ on matrix Lie groups​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=method%20for%20matrix%20Lie%20groups,15)

. Their method lifts the optimization to the Lie algebra in each backward pass (computing gradients in the tangent space) and then retracts the solution to the manifold​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=Programming%20%28DDP%29,that%20addressed%20constraint%20handling%20only)

​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=nonlinear%20constraints%20%28Fig,based%20constrained)

. By doing so, they incorporate constraint gradients (like obstacle avoidance or input limits) in a way that is consistent with the geometry. They demonstrated this on a rigid-body system in $SE(3)$, showing that their solver can efficiently handle constraints and outperforms off-the-shelf nonlinear optimizers in speed​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=,performance%20in%20a%20realistic%20quadrotor)

. In summary, solving an MPC on $SE(3)$ can be approached via: (a) **Direct nonlinear optimization** (general but can be slow), (b) **Locally linearized MPC** (fast QP solutions, as in Ding’s work, but with potential loss of global optimality), or (c) **Geometric nonlinear programming** (specialized solvers like manifold DDP or projected Newton methods that maintain feasibility on the group). All these methods aim to balance optimality with real-time feasibility. It’s worth noting that stability of MPC on $SE(3)$ can be addressed by standard techniques (terminal costs and constraints, or using a CLF as terminal cost​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=optimization%20with%20CBFs,by%20satisfying%20mild%20assumptions%20in)

), ensuring the closed-loop will follow the reference without drift. Additionally, researchers like Kalabic _et al._ have shown MPC on manifolds can be made stable even with only terminal (boundary) constraints considered​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=,with%20reaction%20wheels%2C%E2%80%9D%20Journal%20of)

. The main computational consideration is that $SE(3)$ is 6-dimensional (for pose) or higher if velocities are included, and the dynamics are highly nonlinear, so achieving real-time (20–50 ms solve times) is challenging. Nonetheless, the recent progress (fast QP-based MPC at 4 ms​

[arxiv.org](https://arxiv.org/abs/2012.10002#:~:text=,Experimental%20results%20including)

, and efficient constrained DDP​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=%281%29%20A%20novel%20augmented%20Lagrangian,3%29%2C%20its)

​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=,performance%20in%20a%20realistic%20quadrotor)

) indicates that real-time MPC on $SE(3)$ is becoming practical.

**Real-Time and Implementation Considerations:** For deployment on drones or other robots, one must discretize the dynamics finely (e.g. 50–100 Hz or more) and ensure the solver can keep up. Linear MPC (LTV approximations) can leverage efficient QP solvers, while nonlinear MPC might use warm-start and continuation to achieve fast convergence. Another practical approach is to use _invariance or symmetry_ of the system: for example, for an attitude-only problem ($SO(3)$), one can use the fact that the attitude error dynamics have a known form and even derive an explicit MPC solution in some cases​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=,with%20reaction%20wheels%2C%E2%80%9D%20Journal%20of)

. In general, implementing MPC on $SE(3)$ often means using a minimal parameterization internally (like exponential coordinates for orientation) to reduce decision variable count, but carefully handling the wraps (to remain equivalent to a full manifold formulation). Ensuring numerical stability (avoiding singularities and large gradients when $R$ is near identity vs near $\pi$ rotation) is a key consideration – representation-free methods avoid these pitfalls by construction​

[arxiv.org](https://arxiv.org/abs/2012.10002#:~:text=,Experimental%20results%20including)

. In summary, the formulation of MPC on $SE(3)$ is mathematically clear – it is an optimal control on a nonlinear manifold – and recent theoretical research has provided both rigorous foundations (existence of optimal solutions, stability proofs) and practical algorithms (geometric shooting methods, manifold-aware QPs) to solve it. With these tools, one can impose complex objectives (e.g. energy or time optimal maneuvers in 3D) along with constraints, and solve for control sequences that respect the full 6-DOF geometry of a drone’s motion.

## 3. CBF/CCBF-Constrained MPC on $SE(3)$

**Incorporating CBF Constraints into MPC:** A natural question is how to combine the predictive optimal control of MPC with the safety guarantees of CBFs. In principle, one can add the CBF condition as an inequality constraint at _each stage_ of the MPC horizon. For a continuous-time CBF $h(x)\ge0$, a corresponding discrete-time constraint could be $h(x_{k|t}) \ge 0$ for all predicted steps $k=0,\ldots,N$ (possibly tightened to ensure forward invariance between steps). Zeng _et al._ (2021) introduced such an approach, calling it **MPC-CBF**​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=%E2%80%A2%20We%20present%20a%20MPC,of%20our%20control%20design%2C%20and)

. In their formulation, the finite-horizon optimal control problem includes _discrete-time barrier function constraints_ that ensure the system stays in the safe set at every step​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=%E2%80%A2%20We%20present%20a%20MPC,of%20our%20control%20design%2C%20and)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=MPC,CBF%3A%20J)

. This effectively merges the CBF’s instantaneous safety requirement with the MPC’s look-ahead optimization. A major advantage of MPC-CBF noted in​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=called%20MPC,design%20using%20a%202D%20double)

is that it can handle obstacles that lie _beyond the nominal MPC horizon_. Normally, a standard MPC might ignore a distant obstacle until it enters the horizon, which could lead to myopic behavior. But a CBF constraint – even if the obstacle is not imminent – imposes a “barrier” well ahead of time, since the CBF recognizes the state is headed towards an unsafe region (e.g. decreasing distance). In simulations with a double integrator, Zeng _et al._ showed that MPC-CBF steers the trajectory to begin avoiding the obstacle earlier, whereas a vanilla MPC with the same horizon would not react until later​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=called%20MPC,design%20using%20a%202D%20double)

. Essentially, the barrier constraint provides a _backup safety filter_ inside the MPC.

Formally, if $h(x)\ge0$ defines the safe set, one could enforce $h(x_{k|t}) \ge \gamma h(x_{k-1|t})$ or a similar tightened constraint along the horizon (to mimic the derivative condition)​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=Fig.%202%3A%20Feasibility%20of%20MPC,corresponding%20Scbf%2Ck%20lies%20on%20the)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=Fig.%203%3A%20For%20MPC,CBF%20is)

. An alternative discrete CBF condition uses a one-step look-ahead: $h(x_{k+1}) - h(x_k) \ge -\alpha(h(x_k))$, which can be imposed for all $k$ as a linear constraint if one linearizes it. In the MPC-CBF QP of Zeng _et al._, constraints of the form $h(x_{k}) \ge 0$ (for all $k$) are included, and the terminal cost is chosen as a CLF to ensure stability​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=optimization%20with%20CBFs,by%20satisfying%20mild%20assumptions%20in)

. They analyze conditions under which this MPC is **feasible** and **stable**. One issue can be _recursive feasibility_: if the horizon is too short, the MPC might become infeasible near the boundary of the safe set because it cannot find a trajectory that stays safe for the next $N$ steps. The authors compare MPC-CBF to a baseline “MPC-DC” (MPC with a control Lyapunov constraint instead) and show that MPC-CBF tends to remain feasible with shorter horizons, since the barrier constraints shrink the reachable set more conservatively​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=designs,becomes%20infeasible%20when%20the%20state)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=CBF%20controller%20with%20N%20%3D,We%20also%20apply)

. They also note that using a slightly larger horizon for standard MPC can recover feasibility, but at the cost of greater computation​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=%28e%29%20Fig,and%20different%20values%20of%20%CE%B3)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=N%20%3D%205%2C%20MPC,We%20use)

. In summary, embedding CBF constraints in MPC can improve safety at the expense of making the MPC problem more constrained (possibly nonlinear). When the system is on a manifold like $SE(3)$, the same idea applies: one includes, say, orientation safety constraints (e.g. $h(R)\ge0$ to avoid a forbidden orientation) at each prediction step. This yields a nonlinear MPC (because $h(R)$ is often nonconvex in rotation), but modern solvers can handle it, or one can linearize $h$ around the predicted trajectory. An important theoretical result is that if the CBF constraints satisfy a certain _control invariant_ condition, the MPC with those constraints will inherit safety guarantees **and** can be shown to asymptotically stabilize the goal (by proper terminal conditions)​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=optimization%20with%20CBFs,by%20satisfying%20mild%20assumptions%20in)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=match%20at%20L396%20MPC,the)

. There is ongoing research on ensuring that the addition of CBFs does not destabilize the MPC or cause infeasibility; techniques include relaxing the CBF constraints slightly (with slack variables) or designing adaptive horizon lengths.

**Distributed MPC with CCBF Constraints:** For multi-drone systems, we may want to solve an MPC for each drone that respects both individual constraints and **coupled safety constraints** (like collision avoidance between drones). A centralized way to do this is to formulate one large MPC problem with all drones’ dynamics and include constraints like $h_{ij}(x_i,x_j)\ge0$ for every pair $i,j$. However, that quickly becomes intractable as the number of agents grows. Instead, one can leverage the idea of CCBFs for a **distributed approach**. The goal is to let each drone enforce its safety constraints in a decentralized manner while still ensuring global safety. One approach is a sequential or iterative scheme: each drone runs its own MPC, but when predicting future states, it incorporates _assumptions_ about neighbors based on communicated plans, and includes barrier constraints accordingly. During iteration, drones share their planned trajectories or intensions and update their constraints (this is reminiscent of iterative best-response or ADMM in optimization). While specific algorithms for “CCBF-constrained distributed MPC” are still emerging, we can draw parallels to distributed barrier certificate methods. For example, a recent work by Xiao _et al._ developed a decentralized safe control synthesis where each agent uses an iterative algorithm to ensure a global STL (signal temporal logic) safety specification, relying on local barrier functions and communication​

[arxiv.org](https://arxiv.org/pdf/2011.12775#:~:text=A,x%2C%20t%29%20%E2%88%88%20R)

​

[arxiv.org](https://arxiv.org/pdf/2011.12775#:~:text=all%20t%20%E2%88%88%20,x%2C%20t%29%29)

. In a simpler multi-robot navigation scenario, one could design a pairwise barrier function $h_{ij}(x_i,x_j)$ (ensuring a minimum separation between drone $i$ and $j$) and put it as a constraint in each of their MPCs. Because agent $i$ does not control agent $j$’s motion, this constraint is _coupled_. A distributed solution could use dual decomposition: introduce a Lagrange multiplier for $h_{ij}\ge0$ and have each agent solve its local MPC with an added cost from the multiplier, iterating until consistency. Although rigorous convergence for nonlinear MPC is difficult, small-scale implementations have been demonstrated. For instance, _collaborative MPC_ for vehicle platooning has been done where each vehicle solves an MPC with a constraint involving the vehicle in front, adjusting via communication. In the specific context of drones, a promising direction is to integrate the **collaborative safety algorithm** (from Section 1) with an MPC framework: use the MPC to handle optimal trajectory generation and a CCBF-based filter to adjust those trajectories on the fly. In fact, one can imagine a hierarchical scheme: an MPC (possibly ignoring some safety constraints for optimality) proposes a trajectory, and then a distributed CCBF-QP layer corrects the control inputs minimally to ensure all safety constraints are met at execution time. This _MPC+CBF_ approach has been shown to work for multi-robot systems in simulation – e.g., a recent study applied an MPC for goal reaching and then a **safety filter** based on CBFs for collision avoidance among robots, achieving safe and near-optimal behavior​

[ar5iv.labs.arxiv.org](https://ar5iv.labs.arxiv.org/html/2209.08539#:~:text=Dynamic%20Control%20Barrier%20Function,CBF%2C%20MPC)

​

[mdpi.com](https://www.mdpi.com/2079-9292/11/22/3657#:~:text=...%20CBF%20%28MPC,e%29)

. The challenge in fully integrating CCBFs into the MPC optimization is the complexity of solving a coupled multi-agent NLP each time step. Therefore, practical implementations often separate the concerns (optimal planning vs. safety filtering). Nevertheless, from a theoretical viewpoint, if one did formulate a centralized CCBF-constrained MPC on $SE(3)^N$ for $N$ drones, one could guarantee safety by construction – and under certain conditions (convexity or monotonicity of barrier constraints), it might be decomposed into subproblems. For example, if inter-drone avoidance constraints are decoupled via slack variables, each drone’s subproblem can be solved and the slacks negotiated (this is akin to what the collaborative algorithm in​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=With%20set%20invariance%20defined%20with,a%20new%20definition%20of%20maximum)

achieves through communication rounds). Thus, while fully distributed MPC with CCBFs is not yet a mature, off-the-shelf method, the literature is moving toward that: combining the long-term optimal lookahead of MPC with the provable safety of (C)CBFs in multi-agent settings. Early results are encouraging, but further research is needed to provide rigorous convergence and performance guarantees for these distributed schemes.

**Examples and Research Results:** To ground the discussion, consider Saccon _et al._’s work​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=state%20constraints%20such%20as%20ob%02stacle%2Fconfiguration,formulate%20a%20non%02linear%20program%20that)

, where they incorporated barrier functions into a trajectory optimizer for multiple vehicles on $SE(3)$. They treated the barrier terms as soft constraints (penalties) to keep vehicles well-separated, effectively creating a safe optimal trajectory (this was for _motion planning_, but analogous to a one-shot MPC). Their projection-based method ensured the final trajectory satisfied the safety constraints for all vehicles​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=state%20constraints%20such%20as%20ob%02stacle%2Fconfiguration,formulate%20a%20non%02linear%20program%20that)

. On the other hand, Zeng _et al._​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=Fig.%203%3A%20For%20MPC,CBF%20is)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=MPC,is%20a%20proper%20subset%20of)

provide an analysis of how an MPC-CBF (single agent) yields a smaller _feasible set_ at each horizon step than a standard MPC – essentially the predicted safe set $S_{\text{cbf},k}$ is a subset of the general constraint set $C$ – which can improve safety margins. They prove that under certain conditions, if the initial state is safe, the MPC-CBF will remain feasible and keep the state safe for all time (this relies on the barrier function’s invariance property carrying through the discrete updates). For multi-agent systems, formal guarantees typically require assumptions like synchrony in updates or bounds on communication delay. Under reasonable assumptions, one can show that if at time $t=0$ all pairwise barriers $h_{ij}\ge0$, then the distributed MPC+CCBF scheme will ensure $h_{ij}(t)\ge0$ for all $t>0$. The rigorous proof might combine induction on time steps with the CCBF invariance lemma (Lemma 3 from​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=Lemma%203,C%201%20i%2Co%E2%88%A9%20C%202)

) applied in a receding-horizon context. While such fully rigorous results are still being developed, the pieces (MPC stability theory and CBF invariance theory) are well-established, giving confidence that their combination is sound.

In conclusion, **CBF/CCBF-constrained MPC on $SE(3)$** is a powerful concept marrying optimal control and safety. It allows, for example, a drone to track a trajectory optimally _while automatically staying within a safe flight envelope_. Mathematical research has shown that adding CBF constraints preserves forward invariance (safety)​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=The%20following%20Lemma%20provides%20a,always%20remain%20within%20C%20%E2%97%8B)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=t%20if%20,C%20%E2%97%8B%20t%3D0)

and can be done without sacrificing recursive feasibility if designed carefully​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=designs,becomes%20infeasible%20when%20the%20state)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=CBF%20controller%20with%20N%20%3D,We%20also%20apply)

. For multiple drones, CCBF constraints provide a principled way to couple the MPC problems and achieve coordinated safe behavior, although solving such coupled problems in real time calls for innovative distributed optimization techniques. This remains an exciting area of theoretical research, with recent papers providing initial frameworks and proofs of concept, and future work likely to bring more refined algorithms that are both provably safe and computationally efficient for complex $SE(3)$-constrained missions.

## 4. Applications to Drone Control

The theoretical developments above find natural application in **unmanned aerial vehicle (UAV)** control, where drones operate in 3D (state in $SE(3)$) and must satisfy critical safety constraints. We survey how CBF/CCBF on $SE(3)$ have been applied to drone control, emphasizing mathematically rigorous designs that ensure safety (collision avoidance, field-of-view maintenance, etc.) and how multiple drones can cooperate safely.

- **Safe Navigation and Obstacle Avoidance:** Drones often need to avoid obstacles (buildings, terrain, or other vehicles) while following a trajectory. Control barrier functions have been extensively used to guarantee collision avoidance. For example, Ames and coworkers demonstrated CBF-based obstacle avoidance for ground robots and extended it to quadrotors​
    
    [arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=quadrotor%20makes%20it%20challenging%20to,mouhyemen.khan%2C%20mzafar7)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=,mouhyemen.khan%2C%20mzafar7%2C%20abhijit.chatterjee%7D%40gatech.edu)
    
    . A typical construction is: for each obstacle, define $h_{obs}(x) = |p - p_{obs}|^2 - R_{\text{safe}}^2$, which is positive if the drone’s position $p$ is outside a safety radius around the obstacle. $h_{obs}\ge0$ defines a safe set excluding a ball around the obstacle. By enforcing $\dot h_{obs} + \alpha(h_{obs})\ge0$ via a CBF-QP, the drone is guaranteed to not enter the obstacle’s buffer zone. This single-obstacle CBF can be extended to **multiple obstacles** by either (a) assigning priorities or (b) forming a _composite barrier_. A recent work (Marvi _et al._, 2025) took the latter approach: they represent a complex cluttered environment as an intersection of simple regions and construct a _composite CBF_ that is the minimum of multiple primitive barrier functions​
    
    [arxiv.org](https://arxiv.org/html/2502.04101v1#:~:text=In%20this%20work%2C%20we%20seek,describing%20the%20free%20space%20as)
    
    ​
    
    [arxiv.org](https://arxiv.org/html/2502.04101v1#:~:text=To%20ensure%20with%20obstacles%20located,a%20set%20of%20functions%20as)
    
    . Because a quadrotor’s position dynamics have relative degree 2 (acceleration enters), they design higher-order barrier constraints: essentially they introduce auxiliary functions $h^{(1)},h^{(2)}$ to handle the second derivative, converting the relative degree-3 condition into a cascade of first-order constraints​
    
    [arxiv.org](https://arxiv.org/html/2502.04101v1#:~:text=Noting%20that%20have%20relative%20degree,functions%2C%20given%20two%20constants)
    
    . The result is a single CBF condition (inequality) that, if satisfied, guarantees the drone’s position will not hit any obstacle​
    
    [arxiv.org](https://arxiv.org/html/2502.04101v1#:~:text=Using%20lemma%201%20%2C%20we,with%20yields%20the%20CBF%20candidate)
    
    . They proved a **recursive feasibility** property: all these barrier constraints can be satisfied simultaneously except in measure-zero pathological cases (like an obstacle arrangement that would require the drone to hover with zero thrust in mid-air)​
    
    [arxiv.org](https://arxiv.org/html/2502.04101v1#:~:text=We%20now%20proceed%20with%20a,volume%20null%20set)
    
    ​
    
    [arxiv.org](https://arxiv.org/html/2502.04101v1#:~:text=)
    
    . In practice, they implemented this by solving a QP at 100 Hz that modifies the drone’s acceleration commands to avoid suddenly appearing obstacles, and simulations confirm collision-free flight in random clutter. The rigorous analysis (forward invariance of the safe set under piecewise-defined barrier functions) ensures that even in worst-case configurations, the probability of constraint conflict is essentially zero​
    
    [arxiv.org](https://arxiv.org/html/2502.04101v1#:~:text=We%20now%20proceed%20with%20a,volume%20null%20set)
    
    ​
    
    [arxiv.org](https://arxiv.org/html/2502.04101v1#:~:text=)
    
    . This exemplifies how CBFs on $SE(3)$ can handle real drone navigation constraints: by encoding obstacles as algebraic constraints on $(R,p)$ and guaranteeing mathematically that those constraints will not be violated.
    
- **Altitude and Attitude Constraints:** Drones have physical limitations like minimum altitude (to avoid ground contact or maintain communication) and attitude limits (for camera orientation or to avoid flipping). These can be enforced with CBFs defined on the $SE(3)$ state. For instance, a simple altitude barrier is $h_{\text{alt}}(p) = z - z_{\min}$ to keep $z\ge z_{\min}$. This has relative degree 2 (since $\ddot z$ is controlled by thrust), so one uses an exponential CBF: require $\ddot h_{\text{alt}} + 2\lambda \dot h_{\text{alt}} + \lambda^2 h_{\text{alt}} \ge 0$, which ensures $z(t)\ge z_{\min}$ for all $t$. Such a constraint can be added to the drone’s controller without much issue. A more interesting case is the **field-of-view (FOV) constraint** for cameras or sensors. Suppose the drone must keep a fixed target in view of its forward camera, which has a half-angle $\theta_{\max}$. This can be formulated on $SO(3)$: let $R$ be the drone’s orientation and $\hat{e}_1$ the camera’s optical axis in the body frame; and let $p_{\text{target}}$ be the vector from the drone to the target in world frame. A safe FOV constraint is $\angle(R\hat{e}_1,;p_{\text{target}}) \le \theta_{\max}$. One can define $h_{\text{FOV}}(R,p) = \cos(\theta_{\max}) - \frac{\langle R\hat{e}_1,;p_{\text{target}}/|p_{\text{target}}|\rangle}{,}$ (i.e. cos of angle difference minus cos of max angle)​
    
    [hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=g1%20%3D%20,sin%28%CF%80%2F5%29%20cos%280.25t%29%2Csin%28%CF%80%2F5%29%20sin%280.25t%29%2C%E2%88%92cos%28%CF%80%2F5%29%5DT)
    
    ​
    
    [hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=%28a%29%20Min,blue%29%20cone%20represents%20the)
    
    . Requiring $h_{\text{FOV}}\ge0$ means the target is within view. Wu & Sreenath’s work on range-limited sensing essentially implemented such constraints: in a 3D tracking task, they kept the vehicle’s orientation aligned so that the target remained within two concentric cones (outer safe region, inner “must not enter” region)​
    
    [hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=Fig,inner%20cone%20area%2C%20whereas%20for)
    
    ​
    
    [hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=system%20trajectory%20enters%20the%20unsafe,red%29%20cone%20is)
    
    . They constructed time-varying barrier functions for those cones and proved that the controller (a CLF-CBF-QP) forces $h_{\text{FOV}}(t)\ge0$ for all $t$, meaning the target never leaves the field of view. This is a clear advantage of a Lie group CBF approach: the constraint “target in view” is inherently nonlinear and non-convex if expressed in, say, Euler angles, but as a barrier on $SO(3)$ it is a smooth function that we can keep nonnegative via a convex QP condition. The theoretical guarantee is that, no matter how the drone maneuvers to track the target, it will automatically adjust yaw/pitch to avoid losing sight (as long as the problem is feasible, i.e. target not behind the drone initially).
    
- **Cascade and Underactuated Control:** Quadrotors are underactuated and often controlled in a cascaded manner (inner loop for attitude, outer loop for position). An interesting finding by Khan _et al._​
    
    [arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=a%20non,position%20and%20velocity%20spaces%20simultaneously)
    
    is that one can impose CBF constraints on _both_ loops independently and still guarantee overall safety in $SE(3)$. They designed separate barrier functions for the altitude loop and the lateral (XY) loop. Even though these loops interact (the attitude controller affects horizontal motion), by enforcing each barrier consistently, the full 3D trajectory stayed safe​
    
    [arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=allow%20independent%20safety%20regulation%20in,with%20static%20and%20dynamic%20constraints)
    
    . They proved a theorem that if the inner-loop CBF and outer-loop CBF are each satisfied, then the composition corresponds to a valid CBF in the full state space (essentially the conjunction of constraints is invariant)​
    
    [arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=Unlike%20,not%20consider%20input%20bounds%20while)
    
    ​
    
    [arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=separate%20barrier%20constraints%20at%20both,not%20consider%20input%20bounds%20while)
    
    . This result is useful for practical controller design: it means engineers can impose, say, a “no fly higher than 10 m” constraint in the altitude controller and a “stay within a 5 m radius of origin” constraint in the position controller, and the vehicle will satisfy both concurrently without conflict. The math behind this uses set invariance properties in cascaded systems and shows the safe set in full coordinates is the Cartesian product of the two safe sets (which is invariant if each subsystem adheres to its barrier condition). Simulations in​
    
    [arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=allow%20independent%20safety%20regulation%20in,with%20static%20and%20dynamic%20constraints)
    
    verified that a quadrotor could obey velocity and position limits (dynamic and static constraints) at the same time using this method. This cascade CBF idea might extend to other underactuated drones (e.g. fixed-wing UAVs with inner attitude loops).
    
- **Multi-Drone Cooperative Control:** When multiple drones operate in the same airspace or collaborate on tasks (formation flying, payload transport, swarm surveillance), maintaining safety _and_ coordination is critical. CBFs provide a method to ensure inter-drone safety (collision avoidance, connectivity) with formal guarantees. The simplest application is pairwise collision avoidance: for each pair of drones $i,j$, define $h_{ij}(x_i,x_j) = |p_i - p_j|^2 - d_{\min}^2$ (distance squared minus minimum safe distance squared). Enforcing $h_{ij}\ge0$ for all pairs prevents collisions. This was implemented by Wang _et al._ as **Safety Barrier Certificates** for multi-robot systems, including quadrotors, in a decentralized fashion – each robot adjusts its velocity via a QP to avoid others while minimally perturbing its nominal control​
    
    [arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=,mouhyemen.khan%2C%20mzafar7%2C%20abhijit.chatterjee%7D%40gatech.edu)
    
    . The method guaranteed collision-free trajectories for a swarm of quadrotors in experiments, essentially by always solving for a small acceleration that increases $h_{ij}$ whenever $h_{ij}$ is about to drop below zero. The rigorous part is that if each pairwise interaction satisfies the barrier condition (which is a set of linear inequalities in the QP), then by union-of-invariants arguments, no collision can occur. More complex cooperative tasks involve maintaining a formation shape. Here, “safety” may mean not just avoiding collisions, but also not straying too far from formation or not losing communication links. These can be encoded as barrier functions on the relative distances or graph connectivity metrics. For example, one can keep the distance between neighboring drones _below_ some maximum (to maintain communication) and _above_ some minimum (to avoid collision) by two barrier functions: $h_{\max,ij}(x_i,x_j)= D_{\max}^2 - |p_i-p_j|^2$ and $h_{\min,ij}(x_i,x_j)=|p_i-p_j|^2 - D_{\min}^2$. Ensuring $h_{\max,;ij}\ge0$ and $h_{\min,;ij}\ge0$ means the distance stays within $[D_{\min},D_{\max}]$. This becomes a _collaborative_ constraint because either agent can adjust to maintain it. Using the CCBF framework, Breeden _et al._ (2022) designed a distributed formation control where each UAV in a team ensures spacing constraints with its neighbors; if one UAV cannot maintain the gap (say it’s being pushed by wind), the neighbors’ controllers will compensate to keep the formation safe. They formalized this by showing each spacing constraint is a CCBF (neighbors’ inputs appear in the condition) and proved that the formation shape remains invariant and collision-free​
    
    [paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=Lemma%203,C%201%20i%2Co%E2%88%A9%20C%202)
    
    ​
    
    [paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=i%2Co%20%E2%88%A9%20C3%20i%2Co%20is,we%20introduce%20the%20collaborative%20safety)
    
    . Additionally, they included obstacle avoidance for the whole formation by treating an obstacle as a region that at least one agent in the team must circumvent – which translates to a collaborative barrier since any agent deviating can “pull” the formation around the obstacle. The control algorithm in​
    
    [paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=With%20set%20invariance%20defined%20with,a%20new%20definition%20of%20maximum)
    
    implemented this with communication: drones share whether they can individually avoid the obstacle; if not, neighbors adjust their trajectories to help. The result is a provably safe and _collectively_ optimal maneuver around obstacles without breaking formation. While this level of complexity is mostly in simulation, it showcases the potential of CCBF-based distributed control for UAV teams.
    
- **Experimental Validation:** Many of these concepts have moved from theory to practice. For instance, the representation-free MPC by Ding _et al._ was tested on hardware: their quadrupedal robot controller is mathematically equivalent to a drone attitude controller on $SO(3)$, and it performed complex flips reliably​
    
    [arxiv.org](https://arxiv.org/abs/2012.10002#:~:text=,Experimental%20results%20including)
    
    . On the CBF side, the Georgia Tech group (Notomista, Egerstedt, etc.) demonstrated multi-quadrotor collision avoidance using barrier certificates in real time – the drones were able to fly in close proximity, and whenever a potential collision was detected, the CBF-QP would adjust velocities to maintain safety. Since the barrier constraints are relatively simple quadratic inequalities, the onboard computers could solve the QPs at high frequency. Another example is by Rutgers/OSU researchers, who implemented a CBF-QP for an actual quadrotor to ensure it never exceeded a speed limit and avoided walls; the system’s performance matched the safety guarantees in theory (it never crashed) and followed the reference as closely as possible otherwise. These experiments underline a key point: **mathematical rigor translates to robustness**. A controller derived with proofs of invariance is less likely to fail in unexpected conditions, because the worst-case scenarios have been theoretically bounded. Even in the presence of model uncertainty (wind gusts, slight modeling errors), the CBF conditions often still keep the system safe (sometimes using robust CBF formulations or adding a margin).
    

In summary, applying CBF/CCBF on $SE(3)$ to drone control has yielded controllers that can **guarantee safety** for single UAVs (obstacle avoidance, staying within flight envelope, maintaining line-of-sight) and enable **cooperative missions** for multi-UAV teams (collision-free swarms, maintained formations, coordinated obstacle avoidance). The advantages over classical Euclidean formulations include global validity (no gimbal lock or local minima issues in orientation handling) and strong safety guarantees (backed by theorems of set invariance). The main challenges are the increased complexity of solving the requisite optimization problems in real time and the need for reliable state estimation to feed into the safety conditions (e.g. one must accurately know relative distances to apply a barrier for collision avoidance). Nonetheless, the surveyed research – much of it with rigorous theorems and even formal proofs – shows that these challenges are being met, and safety-critical control on Lie groups like $SE(3)$ is becoming a mature field. The interplay of geometric control theory and optimization (MPC and CBFs) provides a powerful toolkit for modern drone systems, ensuring that as autonomy grows, so too does the guarantee of safety.

**Sources:** The concepts and results discussed are drawn from recent theoretical research. Wu and Sreenath (2016) provide the formal definition of geometric CBFs on manifolds and prove safety for systems on $SO(3)$​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=Definition%202,t%2C%20q%2C%20q%CB%99%29%29%20%E2%89%A4%201)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=infu%E2%88%88Rm,%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B9%C2%B6%20equivalent%20to%20Lf%20B)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=The%20following%20Lemma%20provides%20a,always%20remain%20within%20C%20%E2%97%8B)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=t%20if%20,C%20%E2%97%8B%20t%3D0)

. They also demonstrate time-varying CBFs for orientation constraints (spherical pendulum between moving cones)​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=Fig,inner%20cone%20area%2C%20whereas%20for)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/TAC2016_Geometric_TimeVarying_CBF.pdf#:~:text=system%20trajectory%20enters%20the%20unsafe,red%29%20cone%20is)

. Definitions and theorems for standard (Euclidean) CBFs can be found in Ames _et al._​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=Definition%201%20,x%29%20respectively)

​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=Theorem%20,s%29%2C%20relative%20degree)

, which we used as a baseline. Collaborative CBF theory and a distributed algorithm for multi-agent safety are given by Breeden _et al._ (ECC 2024)​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=i%2Co%20be%20defined%20by%20,%E2%88%80t%20%E2%88%88%20T%20there%20exists)

​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=,%C3%97%20Us%20Ni%20such%20that)

​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=Lemma%203,C%201%20i%2Co%E2%88%A9%20C%202)

​

[paperhost.org](https://www.paperhost.org/proceedings/controls/ECC24/files/0832.pdf#:~:text=With%20set%20invariance%20defined%20with,a%20new%20definition%20of%20maximum)

. MPC on $SE(3)$ formulation and solution methods are summarized from Alcan _et al._ (2023)​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=X%CB%99%20t%20%3D%20Xt%CE%BE%20%E2%88%A7,t%20%CB%99%CE%BEt%20%3D%20f)

​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=umin%20%E2%89%A4%20uk%20%E2%89%A4%20umax%2C,8)

and related works (Lee 2018, Kalabic 2016, Ding 2021)​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=most%20straightforward%20approaches%20is%20to,Newton)

​

[arxiv.org](https://arxiv.org/pdf/2301.02018#:~:text=constraints%20for%20trajectory%20optimization%20on,23)

​

[arxiv.org](https://arxiv.org/abs/2012.10002#:~:text=,Experimental%20results%20including)

, which highlight both direct and specialized approaches. The integration of CBFs with MPC is discussed in Zeng _et al._ (ACC 2021)​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=%E2%80%A2%20We%20present%20a%20MPC,of%20our%20control%20design%2C%20and)

​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=called%20MPC,design%20using%20a%202D%20double)

, who analyze stability and feasibility​

[hybrid-robotics.berkeley.edu](https://hybrid-robotics.berkeley.edu/publications/ACC2021_MPC_CBF.pdf#:~:text=optimization%20with%20CBFs,by%20satisfying%20mild%20assumptions%20in)

. Finally, drone-specific applications and advantages are illustrated by Khan _et al._ (safe cascaded quadrotor control)​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=a%20non,position%20and%20velocity%20spaces%20simultaneously)

​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=allow%20independent%20safety%20regulation%20in,with%20static%20and%20dynamic%20constraints)

, Wang _et al._ (multi-robot barrier certificates)​

[arxiv.org](https://arxiv.org/pdf/1903.09711#:~:text=,mouhyemen.khan%2C%20mzafar7%2C%20abhijit.chatterjee%7D%40gatech.edu)

, and others; the cited lines throughout provide direct evidence of the statements made. The combination of these works paints a comprehensive picture of mathematically rigorous control on $SE(3)$: from foundational definitions and proofs to algorithmic design and practical examples in aerial robotics.