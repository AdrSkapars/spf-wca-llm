from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
j = Int('j')

# 'in_[i] < in_[i-1]' constraints
pred1 = ForAll([i], Implies(And(i > 0, i <= (N-1), i%2==1), ss(i) < ss(i-1)))

# 'in_0 < in_[i]' constraints
pred2 = ForAll([i], Implies(And(i > 2, i <= (N-1), i%2==1), ss(0) < ss(i)))

# 'in1 < in0' constraint
pred3 = Implies(N > 1, ss(1) < ss(0))

# 'in_[i-2] < in_[i]' constraints
pred4 = ForAll([i], Implies(And(i >= 4, i < N, i%2==0), ss(i-2) < ss(i)))

prediction = And(pred1, pred2, pred3, pred4)


########

i = Int('i')
# {ss[1] < ss[0] | 2 <= N}
# (2 <= N) -> (ss[1] < ss[0])
truth1 = Implies(2 <= N, ss(1) < ss(0))

# when N=4, its 0 <= i <= 1, condition holds for i=0
# when N=5, its 0 <= i <= 1, condition holds for i=0
# when N=6, its 0 <= i <= 3, condition holds for i=0,2
# when N=7, its 0 <= i <= 3, condition holds for i=0,2
# when N=8, its 0 <= i <= 5, condition holds for i=0,2,4
# when N=9, its 0 <= i <= 5, condition holds for i=0,2,4
# {ss[i] < ss[i+3] < ss[i+2] | 0 <= i <= N-(3+N%2) and 4 <= N and i%2 == 0} for all i in Z+
# for all i, (0 <= i <= N-(3+N%2) and 4 <= N and i%2 == 0) -> (ss[i] < ss[i+3] < ss[i+2])
truth2 = ForAll([i], Implies(And(0 <= i, i <= N-(3+N%2), 4 <= N, i%2 == 0), And(ss(i) < ss(i+3), ss(i+3) < ss(i+2))))

# {ss[N-3] < ss[N-1] | 3 <= N and N%2 == 1}
# (3 <= N and N%2 == 1) -> (ss[N-3] < ss[N-1])
truth3 = Implies(And(3 <= N, N%2 == 1), ss(N-3) < ss(N-1))
truth = And(truth1, truth2, truth3)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)