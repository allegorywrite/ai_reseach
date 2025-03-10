Consensus-Based Control Barrier Function for Swarm*
Manao Machida and Masumi Ichien
Abstract — In swarm control, many robots coordinate their
actions in a distributed and decentralized way. We propose a
consensus-based control barrier function (CCBF) for a swarm.
CCBF restricts the states of the whole distributed system,
not just those of the individual robots. The barrier function
is approximated by a consensus ﬁlter. We prove that CCBF
constrains the control inputs for holding the forward invariance
of the safety set. Moreover, we applied CCBF to a practical
problem and conducted an experiment with actual robots. The
results showed that CCBF restricted the states of multiple
robots to the safety set. To the best of our knowledge, this is
the ﬁrst CBF that can restrict the state of the whole distributed
system with only local communication. CCBF has various
applications such as monitoring with a swarm and maintaining
the network between a swarm and a base station.
## I. INTRODUCTION
The control barrier function (CBF), proposed by [1],
imposes inequality constraints on the control input for holding forward invariance of a safety set. The safety set is
represented by a function that provides the constraint of
control inputs. [2] proposed a CBF using a quadratic program
(QP) for selecting an optimal control input.
In swarm control, many robots coordinate their actions
in a distributed and decentralized way [10]. The robots
are relatively simple and have only local communication
and sensing capabilities. Consensus [11], [12], formation
- [13], [14], [15] and coverage [16], [17] problems have been
studied in swarm control. Swarm control has applications
such as waste management [18] and search tasks [19].
Moreover, in swarm control, communication networks need
to be maintained [20], [21], [22].
A CBF can be applied to a single robot [3], [4], [5] or
to multiple robots [6], [7], [8], [9]. The existing work on
CBFs in swarms aims at avoiding collisions [6], [8], [9]
and maintaining connectivity [7] between the robots. These
barrier functions restrict the distance between pairs of robots
and depend on only the local state, that is, each robot’s
own state and nearby robots’ states. Hence, these CBFs for
swarms cannot restrict the states of the whole swarm.
In this paper, we propose consensus-based CBF (CCBF),
which can restrict the states of swarm robots to a safety set
by using only local interactions between the robots. CCBF
can incorporate various barrier functions that depend on the
state of the whole swarm. Hence, it can restrict not only a
single robot’s state but also a swarm’s one to a safety set.
To the best of our knowledge, this is the ﬁrst CBF that can
*This work was not supported by any organization
Manao Machida and Masumi Ichien are with Data Science Research Laboratories, NEC Corporation, Kawasaki, Kanagawa, Japan
manaomachida@nec.com, m-ichien@nec.comrestrict the states of a whole distributed system with only
local communication. CCBF has various applications such as
monitoring with a swarm, maintaining the network between
a swarm and a base station. In CCBF, the value of the barrier
function is approximated by a consensus ﬁlter. The consensus
ﬁlter [23], [24] is a distributed algorithm that allows the
nodes of a sensor network to track the average of all of their
measurements. We prove that CCBF provides the constraint
on the control inputs for holding forward invariance of the
safety set. We applied CCBF to a practical problem, i.e.,
maintaining the network between a swarm and a base station
and conducted an experiment with actual robots; we found
that CCBF is effective on this practical problem.
Our contributions are as follows:
We propose CCBF, which can restrict not a single
robot’s state but the whole swarm’s state to a safety
set by using only local interactions between the robots.
We applied CCBF to a practical problem and showed
that it is effective for swarm control.
## II. P RELIMINARIES
LetR=f1;:::;ngbe a set ofnrobots. Robot i2Rhas
a statexi2Xi, whereXiis the state space of robot i. The
state of all of the robots is denoted by x= [xT
1;:::;xT
n]T,
and a combination of state spaces of the robots is denoted
byX=i2RXi. We refer to the state of all of the robots
as the swarm state.
LetC Xbe a nonempty compact safety set and h:
C! Rbe as follows:
h(x)>0 (x2Int(C )) (1)
h(x) = 0 (x2@C) (2)
@h
@x(x)6= 0 (x2@C); (3)
where Int(C )is the interior of C, and@C=CnInt(C ). We
assume thatCXis forward invariant if x(t)2C holds
for allt2[0;1)whenx(0)2C.
The barrier function is deﬁned as follows:
Deﬁnition 1: Consider a nonlinear system:
_x=f(x): (4)
A continuously differential his a zeroing barrier function
(ZBF) if there exists 
 > 0that satisﬁes the following
condition for all x2C.
_h(x) 
h(x): (5)
Ifhis a ZBF, then the safety set Cis forward invariant under
the dynamics (4).
978-1-7281-9077-8/21/$31.00 ©2021 IEEE
2021 IEEE International Conference on Robotics and Automation (ICRA 2021)
May 31 - June 4, 2021, Xi'an, China
8623
2021 IEEE International Conference on Robotics and Automation (ICRA) | 978-1-7281-9077-8/21/$31.00 ©2021 IEEE | DOI: 10.1109/ICRA48506.2021.9561971
Authorized licensed use limited to: Keio University. Downloaded on March 08,2025 at 11:32:01 UTC from IEEE Xplore. Restrictions apply. We use CBF for safety control. Let Ube a set of control
inputs. Consider an afﬁne control system:
_x=f(x) +g(x)u; (6)
whereu2U.
The CBF controller for safety control is deﬁned as follow:
Deﬁnition 2: Consider the control system (6) and a feedback controller u=k(x). A control input based on the CBF
controller is as follows:
u(x)2arg min
u2Ujju k(x)jj2
s:t:_h(x) 
h(x);(7)
where
 >0.
The control input u(x)keeps the state of the robot in the
safety set.
The robots have local communication capabilities. Let
G= (R;E)be an undirected connected communication
graph. Robots i;j2Rcan communicate if (i;j)2Eholds.
LetNi=fj2Rj(i;j)2Egbe the set of robots that are
adjacent to robot i.
A consensus ﬁlter [23], [24] is a distributed algorithm that
allows the nodes of a sensor network to track the average of
all of their measurements. The high-pass consensus ﬁlter is
as follows [23]:
_yi=X
j2Ni(yj yi) + _zi
yi(0) =zi(0);(8)
whereziis a signal measured by sensor (robot) i. The
consensus ﬁlter allows yi(t)to track1
nP
j2Rzj(t). It is
important thatP
i2Ryi(t) =P
i2Rzi(t)holds becauseP
i2R_yi=P
i2R_ziholds.
## III. R ELATED WORK
The existing work on CBFs in swarms aims at avoiding
collisions [6], [8], [9] and maintaining connectivity [7] between the robots. In these studies, the CBFs depend on only
local information and restrict the distance between any two
robots. For example, the CBF (reciprocal barrier function)
for collision avoidance between robots i2Randj6=iin
- [6] is as follows:
hij=(pi pj)T
jjpi pjjj(vi vj) +q
4amax(jjpi pjjj Ds)
Bij=1
hij
wherepi;viare the position and velocity of robot i, respectively.Bijis a reciprocal barrier function for collision
avoidance between robots iandj.Ds>0is safety distance.
Roboti’s control input uisatisﬁesjjuijjamax. [6] also
described how to design the neighbor set of each robot. They
deﬁned the neighbor set of robot ias follows:
Ni=8
<
:j6=ijjpi pjjjDs+1
4amax 4amax

1
3
+ 2v max!29
=
;;wherevmax is the velocity limits of the robots, 
 >0.
In their method, the swarm can avoid collisions between
the robots by using Bijonly ifj2Niholds. Hence, their
CBFs may depend on only local states, that is, the robot i’s
state and one of the other robots near robot i. These CBFs
are useful in the distributed system. However, how to use a
CBF that depends on the whole state in a distributed system
is an open problem.
In our method, we consider a CBF that depends on the
whole swarm’s state. CCBF has various applications besides
avoiding collisions. In section V, we describe an application
of CCBF.
## IV. C ONSENSUS -BASED CONTROL BARRIER FUNCTION
Let us consider the following ZBF.
B(x) =X
m2Mm(X
i2Rim(xi)) (9)
where m:Rlm!Randim:Xi!Rlmare
differentiable, lmis an arbitrary natural number, and M=
f1;:::;Mg.Mis an arbitrary integer. This representation
includes the simplest form of the Kolmogorov–Arnold representation theorem [25], [26], so that various functions can
be represented by (9).
Now let us show how to use our representation (9).
Example 1: Consider a safety set based on the task success probability. Let pi(xi)be the probability that robot
i2Rhaving state xi2Xicompletes the task. A ZBF
is as follows:
B(x) = 1 (1 p1(x1))(1 p2(x2)) q: (10)
If a swarm’s state is in the safety set corresponding to this
ZBF, then the swarm completes the task with a q0or
more probability.
This ZBF is represented by (9) as follows:
B(x) =1 q+1
2f(1 p1(x1)) + (1 p2(x2))g2
 1
2
(1 p1(x1))2+ (1 p2(x2))2	
;(11)
that is,
1(c) = 1 q+1
2c2
11(x1) = 1 p1(x1); 21(x2) = 1 p2(x2)
2(c) = 1
2c
12(x1) = (1 p1(x1))2; 22(x2) = (1 p2(x2))2(12)
wherec2R; M =f1;2g; l 1=l2= 1.
The time derivative of ZBF (9) is
_B(x) =X
i2RX
m2Mrm(X
j2Rjm(xj))T@im
@xi(xi)T_xi;
(13)
wherermis the gradient of m. If each robot i2Rin a
swarm satisﬁes the following condition,
X
m2Mrm(X
j2Rjm(xj))T@im
@xi(xi)T_xi 
B(x) (14)
8624Authorized licensed use limited to: Keio University. Downloaded on March 08,2025 at 11:32:01 UTC from IEEE Xplore. Restrictions apply. 1m(x1) y1mx1 k1(x1) u1
x1Robot 1
im(xi) yimxi ki(xi) ui
xiRoboti
nm(xn) ynmxn kn(xn) un
xnRobotn
**Fig. 1:** CCBF controller
then _B(x)n
B(x) holds. However,P
j2Rjm(xj)
depends on the whole swarm’s state x2X.
Figure 1 shows a CCBF controller, where uiis the control
input of robot i2R.
In CCBF, each robot approximatesP
j2Rjm(xj) (m2
M)by using a consensus ﬁlter. Robot i2Rmeasuresim(xi) (m2M), and the consensus ﬁlter allows the robots to track the average of their measurements, that is,1
nP
j2Rjm(xj). The information transmitted between robots iandj2 Niis[yi1;:::;yiM]
and[yj1;:::;yjM]. Hence, each robot i2RapproximatesP
j2Rjm(xj)using only local information: xi,
[yi1;:::;yiM], and [yj1;:::;yjM] (8j2Ni).
CCBF is as follows:
Consensus Filter
_yim=kLX
j2Ni(yjm yim) +_im(xi)
yim(0) =im(xi(0));(15)
wherekL>0is the gain of the consensus.
CBF Controller
ui(xi)2arg min
uijjui ki(xi)jj2
s:t:X
m2Mrm(nyim)T_im(xi) 
X
m2Mm(nyim)
(16)
LetB=fy2RnMjP
i2RP
m2Mm(nyim)0g. The
following is a theorem on the forward invariance of the safety
set.
**Theorem 1:** Ifmis concave for all m2M, thenCB
is forward invariant under CCBF (15), (16).The proof of this theorem is shown in Appendix A. Theorem
1 shows that CCBF restricts the swarm’s state x2X
to a safety setC. The forward invariant set CB is
similar toC RnMafter a sufﬁcient time passes, becauseP
m2Mm(nyim)tracksB(x). This means that the swarm’s
state can reach almost all states in C.
LetB+=fy2RnMj8i2R;m(nyim)0g. WhenB
is represented by B(x) = (P
i2Ri(xi))andi:Xi!
R, the following theorem holds.
**Theorem 2:** LetB(x) = (P
i2Ri(xi))andi:Xi!
#### R. If is monotone, then CB +is forward invariant under
CCBF (15), (16).
The proof of this theorem is shown in Appendix B. Theorem
2 shows that CCBF restricts a swarm’s state to the safety set
even if the ZBF is monotone and not concave in the special
caseB(x) = (P
i2Ri(xi))andi:Xi!R.
## V. E XAMPLE
Let us introduce an application of CCBF: maintaining a
network between a swarm and a base station.
This problem is considered in [27]. In [27], some robots
must be proximal to the base station to receive instructions.
In this example, we introduce an ”OR” constraint and a
constraint on the probability. We can easily apply these constraints to other problems. For example, the monitoring task
with a swarm in which at least one robot keeps monitoring
the object can be represented by the ”OR” constraint.
#### A. ”OR” constraint
First, let us consider a simple communication model.
Roboti2Rcan communicate with the base station if
xi2Ci=fxi2Xijjjxi ojjrgholds, where xi;oare
positions of robot iand the base station, respectively. If at
least one robot can communicate with the base station, then
the whole swarm can receive messages from the base station
through a multi-hop network in the swarm. Hence, the swarm
in the safety setC=fx2Xj9i2R;xi2Cigmaintains
communication with the base station. This constraint is an
”OR” constraint, that is, it requires that at least one robot
satisﬁes the constraint for itself. Let h(xi) =r2 jjxi ojj2.
The ZBF (9) is as follows:
B(x) =X
i2Ri(xi) (17)
(c) =c (18)
i(xi) =
h(xi) (xi2Ci)
0 (xi2XinCi))(19)
iis not differentiable on xi2@Ci, so we use the following
dinstead of@i
@xito restrict the control input.
d(xi) =@h
@xi(xi) (xi2Ci)
0 (xi2XinCi))(20)
The constraint (16) using dis as follows:
d(xi)T_xi 
(nyi) (21)
This CCBF restricts the swarm’s state to the safety set
because of Theorem 1.
8625Authorized licensed use limited to: Keio University. Downloaded on March 08,2025 at 11:32:01 UTC from IEEE Xplore. Restrictions apply. −1 0 1
0.0s−101
−1 0 1
0.5s−101
−1 0 1
1.0s−101
−1 0 1
1.5s−101
−1 0 1
2.0s−101
−1 0 1
2.5s−101
−1 0 1
3.0s−101
−1 0 1
3.5s−101
−1 0 1
4.0s−101Fig. 2: State of swarm under CCBF with 
=kL= 5
for maintaining network between swarm and base station.
Each robot in a red circle can communicate with the base
station. The black circle represents the destination of the
robots; small circles represent positions of the robots; and
green lines show the communication network in the swarm.
Figure 2 shows a numerical simulation of CCBF for
maintaining the network between the swarm and the base
station. All robots in the swarm head for their destination,
represented by the black circle. Then, one robot stays in
Cirepresented by a red circle, and the others reach their
destination. This means that CCBF maintains a network
between the swarm and the base station while allowing the
swarm to move as much as possible.
#### B. Constraint on Probability
Now let us consider a more complex communication
model. Here, we assume that p(xi)is the success rate of
communication between robot iand the base station. The
safety setCis the set of states in which the success rate of
communication between the swarm and the base station is
not less than q>0.
C=fx2Xj(1 i2R(1 p(xi)))qg (22)
The ZBF forCis as follows:
B(x) = (1 i2R(1 p(xi))) q (23)
This function is represented by
(c) = 1 ec q (24)
i(xi) = log(1 p(xi)): (25)
This CCBF restricts the swarm’s state to the safety set
because of Theorem 2.
Figure 3 shows a numerical simulation of CCBF for the
success rate of communication between the swarm and the
base station. The settings of the simulation are the same as in
Fig.2 except for the value of kL. In Fig. 3, the approximate
values (nyi)for eachi2Rtrack the true ZBF value B(x).
It shows that the consensus ﬁlter in our method is useful to
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
time (s)0.00.20.40.60.81.0
V
alues of ZBF
**Fig.
3:** Comparison of true ZBF value and approximate ZBF
values under CCBF with 
= 5,kL= 20,q= 0:1. The
solid red line shows the true ZBF value B(x(t)), and each
dash-dotted line shows an approximate ZBF value (nyi(t))
ofi2R.
0.0s
 10.0s
20.0s
 30.0s
**Fig.
4:** State of swarm in experiment on CCBF with eight
robots. A red circle shows a area where at least one robot
needs to stay; and a black square represents a destination of
robots.
approximate true ZBF value. Moreover, mini2R(nyi(t))
B(x(t)) holds for all t0. This is an important property
in the proof of Theorem 2. This CCBF satisﬁes B(x(t))
mini2R(nyi(t))0fort0, that is, it restricts the
swarm’s state to the safety set.
## VI. E XPERIMENTAL RESULTS
We conducted an experiment on a robot operating system
(ROS) and Turtlebot3 Burger. Turtlebot3 Burger is a nonholonomic robot, and the control input of robot i2R
representsui= (uvi;uwi)T2R2, where (vi;wi)T=ui,
andviandwiare the velocity and angular velocity of
roboti, respectively. In addition, uvi2[0:0;0:1] anduwi2
[ 1:0; 1:0] hold.
Figure 4 shows the swarm state with eight robots. Note that
the experiment is described in Section V-A. The robots in the
red circle can communicate with the base station. All robots
head for their destination represented by the black square.
8626Authorized licensed use limited to: Keio University. Downloaded on March 08,2025 at 11:32:01 UTC from IEEE Xplore. Restrictions apply. Leto;xibe positions of destination and robot i, respectively.
Moreover, we deﬁne a set of safety transfer vectors Wand
a set of velocities Wvas follows: any zi2W satisﬁes
X
m2Mrm(nyim)T@im
@xi(xi)Tzi 
X
m2Mm(nyim)
(26)
and anyuvi2Wvsatisﬁes
X
m2Mrm(nyim)T@im
@xi(xi)Tcos(i)
sin(i)
uvi
 
X
m2Mm(nyim);(27)
whereiis the orientation of robot i. We calculated the
control input as follows:
ki(xi) =ku(o xi) (28)
zi2arg min
z0
i2Wjjz0
i ki(xi)jj (29)
u
vi= [cos(i)sin(i)]zi (30)
uwi= kw6cos(i)
sin(i)0
0
zi (31)
uvi2arg min
u0
vi2Wvu0
vi u
vi; (32)
where6abc(a;b;c2R2)represents an angle in a circular
measure formed by vector a bandc b, andku;kw>0is
the gain. Each robot communicates with three other robots,
that is,jNij= 3 (8i2R). In Figure 4, one robot stays in
the red circle; this means CCBF restricted the eight robots
to the safety set with only local communication.
## VII. C ONCLUSION
We proposed a consensus-based control barrier function
(CCBF) for a swarm. CCBF can restrict the states of a
whole distributed system to a safety set with only local
communication in the system. Our method restricts not only
the states of the individual robots; it also restricts the state
of the whole swarm to a safety set. In CCBF, the value of
a barrier function is approximated by a consensus ﬁlter. We
proved that CCBF provides the constraint of control inputs
for holding forward invariance of the safety set. We also
applied CCBF to the practical problem and conducted the
experiment with actual robots. The results showed that CCBF
can restrict the states of the multiple robots to a safety set.
In this paper, we showed how to calculate the inequality
constraints on the basis of a CBF for the distributed system.
However, we did not discuss whether there exists a control
inputu2Uthat satisﬁes the inequality constraints on the
basis of CCBF. Thus, one possible direction for future work
is to study a class of consensus-based ZBFs which satisfy
the following condition: for all (x;y)2(C;B), there exists
u2Usuch that _(nyi) 
(nyi)holds.APPENDIX
#### A. Proof of Theorem 1
The inequality,
X
i2R1
nm(nyim)m(X
i2Ryim) = m(X
i2Rim(xi))
holds because m(m2M)is concave and because
of the properties of the consensus ﬁlterP
i2Ryim=P
i2Rim(xi). LetV(y) =P
m2MP
i2Rm(nyim). Obviously,V(y)nB(x)holds. The time derivative of Vin
CCBF (15) and (16) is
_V(y) =X
m2MX
i2Rrm(nyim)Tn_yim
= nkLX
m2MX
i2RX
j2Nirm(nyim)T(yim yjm)
+nX
i2RX
m2Mrm(nyim)T_jm(xi)
  nkLX
m2MX
i2RX
j2Nirm(nyim)T(yim yjm)
 n
V (y):
The following condition holds for the ﬁrst term.
Wm=X
i2RX
j2Nirm(nyim)T(yim yjm)
=X
(i;j)2E1
2(rm(nyim) rm(nyjm))T(yim yjm)
Moreover, (rm(a) rm(b))T(a b)0holds because
mis concave. Thus, _V(y) n
V(y)holds.
If(x(0);y (0))2CB holds thenB(x(t))1
nV(y(t))
0 holds for all t2[0;1). Hence,CB is forward invariant.
#### B. Proof of Theorem 2
We will show that _(nyi) n
(nyi)holds for all
i2arg minj2R(nyj). Leti2arg minj2R(nyj). The
time derivative of in CCBF (15) and (16) is
_(nyi) =r(nyi)Tn_yi
=r(nyi)TnkLX
j2Ni(yj yi) +r(nyi)Tn_i(xi):
The ﬁrst term is larger than 0because 1) if is monotonically increasing, then r(nyi)0holds andyjyiholds
for allj2R, or 2) if is monotonically decreasing, then
r(nyi)0holds andyjyiholds for all j2R. Thus,
the following condition holds.
_(nyi)nr(nyi)T_i(xi) n
(nyi)
Ify(0)2B+, then mini2R(nyi(t))0holds for all t2
[0;1).mini2R(nyi)(P
i2Ri(xi))holds because 
is monotonic and there exists j;k2Rsuch thatnyjP
i2Ri(xi)nykholds. Hence, if (x(0);y (0))2CB +,
then(P
i2Ri(xi(t)))0holds for all t2[0;1).
8627Authorized licensed use limited to: Keio University. Downloaded on March 08,2025 at 11:32:01 UTC from IEEE Xplore. Restrictions apply. REFERENCES
- [1] P. Wieland and F. Allg ¨ower, “Constructive safety using control barrier functions,” IFAC Proceedings Volumes,
vol. 40, no. 12, pp. 462 – 467, 2007, 7th IFAC
Symposium on Nonlinear Control Systems. [Online]. Available:
http://www.sciencedirect.com/science/article/pii/S1474667016355690
- [2] A. D. Ames, X. Xu, J. W. Grizzle, and P. Tabuada, “Control barrier
function based quadratic programs for safety critical systems,” IEEE
Transactions on Automatic Control, vol. 62, no. 8, pp. 3861–3876,
### Aug 2017.
- [3] Q. Nguyen, A. Hereid, J. W. Grizzle, A. D. Ames, and K. Sreenath, “3d
dynamic walking on stepping stones with control barrier functions,”
in2016 IEEE 55th Conference on Decision and Control (CDC), Dec
2016, pp. 827–834.
- [4] G. Wu and K. Sreenath, “Safety-critical control of a planar quadrotor,”
in2016 American Control Conference (ACC), July 2016, pp. 2252–
### 2258.
- [5] X. Xu, T. Waters, D. Pickem, P. Glotfelter, M. Egerstedt, P. Tabuada,
#### J. W. Grizzle, and A. D. Ames, “Realizing simultaneous lane keeping
and adaptive speed regulation on accessible mobile robot testbeds,”
in2017 IEEE Conference on Control Technology and Applications
(CCTA), Aug 2017, pp. 1769–1775.
- [6] U. Borrmann, L. Wang, A. D. Ames, and M. Egerstedt,
“Control barrier certiﬁcates for safe swarm behavior,” IFACPapersOnLine, vol. 48, no. 27, pp. 68 – 73, 2015, analysis
and Design of Hybrid Systems ADHS. [Online]. Available:
http://www.sciencedirect.com/science/article/pii/S240589631502412X
- [7] L. Wang, A. D. Ames, and M. Egerstedt, “Multi-objective compositions for collision-free connectivity maintenance in teams of mobile
robots,” in 2016 IEEE 55th Conference on Decision and Control
(CDC), Dec 2016, pp. 2659–2664.
- [8] L. Wang, A. D. Ames, and M. Egerstedt, “Safety barrier certiﬁcates for
collisions-free multirobot systems,” IEEE Transactions on Robotics,
vol. 33, no. 3, pp. 661–674, June 2017.
- [9] D. Pickem, P. Glotfelter, L. Wang, M. Mote, A. Ames, E. Feron, and
#### M. Egerstedt, “The robotarium: A remotely accessible swarm robotics
research testbed,” in 2017 IEEE International Conference on Robotics
and Automation (ICRA), May 2017, pp. 1699–1706.
- [10] I. Navarro and F. Mat ´ıa, “An introduction to swarm robotics,” ISRN
Robotics, vol. 2013, 09 2012.
- [11] M. A. Joordens and M. Jamshidi, “Consensus control for a system of
underwater swarm robots,” IEEE Systems Journal, vol. 4, no. 1, pp.
65–73, March 2010.
- [12] Y . Zheng, Y . Zhu, and L. Wang, “Consensus of heterogeneous multiagent systems,” IET Control Theory Applications, vol. 5, no. 16, pp.
1881–1888, November 2011.
- [13] F. E. Schneider and D. Wildermuth, “A potential ﬁeld based approach
to multi robot formation navigation,” in IEEE International Conference on Robotics, Intelligent Systems and Signal Processing, 2003.
Proceedings. 2003, vol. 1, Oct 2003, pp. 680–685 vol.1.
- [14] J. Dai, S. Wang, Y . Jang, X. Wu, and Z. Cao, “Multi-uav cooperative
formation ﬂight control based on apf amp; smc,” in 2017 2nd International Conference on Robotics and Automation Engineering (ICRAE),
Dec 2017, pp. 222–228.
- [15] J. Ghommam, M. Saad, and F. Mnif, “Robust adaptive formation control of fully actuated marine vessels using local potential functions,”
in2010 IEEE International Conference on Robotics and Automation,
May 2010, pp. 3001–3007.
- [16] A. Howard, M. J. Matari ´c, and G. S. Sukhatme, “Mobile sensor
network deployment using potential ﬁelds: A distributed, scalable
solution to the area coverage problem,” in Distributed Autonomous
Robotic Systems 5, H. Asama, T. Arai, T. Fukuda, and T. Hasegawa,
Eds. Tokyo: Springer Japan, 2002, pp. 299–308.
- [17] Y . S. Hanay and V . Gazi, “Sensor coverage maximization with
potential ﬁelds,” in 2014 IEEE Symposium on Computers and Communications (ISCC), June 2014, pp. 1–6.
- [18] A. L. Alfeo, E. C. Ferrer, Y . L. Carrillo, A. Grignard, L. A. Pastor,
#### D. T. Sleeper, M. G. C. A. Cimino, B. Lepri, G. Vaglini, K. Larson,
#### M. Dorigo, and A. S. Pentland, “Urban swarms: A new approach for
autonomous waste management,” 2019 International Conference on
Robotics and Automation (ICRA), pp. 4233–4240, 2018.
- [19] M. G. C. A. Cimino, A. Lazzeri, and G. Vaglini, “Using differential
evolution to improve pheromone-based coordination of swarms of
drones for collaborative target detection,” in ICPRAM, 2016.[20] M. Ji and M. Egerstedt, “Distributed coordination control of multiagent systems while preserving connectedness,” IEEE Transactions on
Robotics, vol. 23, no. 4, pp. 693–703, Aug 2007.
- [21] A. Ajorlou, A. Momeni, and A. G. Aghdam, “A class of bounded
distributed control strategies for connectivity preservation in multiagent systems,” IEEE Transactions on Automatic Control, vol. 55,
no. 12, pp. 2828–2833, Dec 2010.
- [22] D. Cai, S. Wu, and J. Deng, “Distributed global connectivity maintenance and control of multi-robot networks,” IEEE Access, vol. 5, pp.
9398–9414, 2017.
- [23] D. Spanos, R. Olfati-saber, and R. Murray, “Dynamic consensus on
mobile networks,” 16th IFAC World Congr., 01 2005.
- [24] R. Olfati-Saber and J. Shamma, “Consensus ﬁlters for sensor networks
and distributed sensor fusion,” in Proceedings of the 44th IEEE
Conference on Decision and Control, vol. 2005, 01 2006, pp. 6698 –
### 6703.
- [25] A. Kolmogorov, “On the representation of continuous functions of
several variables by superpositions of continuous functions of a
smaller number of variables,” in Proceedings of the USSR Academy
of Sciences, vol. 108, 1956, pp. 179–182.
- [26] V . I. Arnold, “On functions of three variables,” in Proceedings of the
USSR Academy of Sciences, vol. 114, 1957, pp. 679 – 681.
- [27] P. Mukhija, R. Sawhney, and M. Krishna, “Multi robotic exploration
with communication requirement to a ﬁxed base station.” in Proceedings of the 9th International Conference on Autonomous Agents and
Multiagent Systems, 01 2010, pp. 1515–1516.
8628Authorized licensed use limited to: Keio University. Downloaded on March 08,2025 at 11:32:01 UTC from IEEE Xplore. Restrictions apply. 