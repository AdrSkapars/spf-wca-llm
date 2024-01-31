from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# ss[i] < ss[i - 1], for i = 1 and i = 0
constraints1 = ForAll([i], And(i == 1, ss(i) < ss(i - 1))) 
constraints2 = ForAll([i], And(i == 0, ss(i) < ss(3)))

# ss[N - 1] < ss[N - 2], for N >= 4
constraints3 = ForAll([N], Implies( N >= 4, ss(N - 1) < ss(N - 2)))

# ss[N - 3] < ss[N - 4], for N not a multiple of 4 and N >= 5
constraints4 = ForAll([N], Implies(And(N % 4 != 0, N >= 5), ss(N - 3) < ss(N - 4)))

# ss[N - 2] < ss[N - 1], if N is a multiple of 4
# ss[N - 2] < ss[N - 3], if N is not a multiple of 4
# for all N >= 5
constraints5 = ForAll([N], Implies(N >= 5,
                                    If(N % 4 == 0, ss(N - 2) < ss(N - 1), ss(N - 2) < ss(N - 3))))

# Final specification
prediction = And(constraints1, constraints2, constraints3, constraints4, constraints5)


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