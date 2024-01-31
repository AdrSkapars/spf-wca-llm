from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

from z3 import *

# Define integer and array
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

# Define variables i, j, k to manipulate
i = Int('i')
j = Int('j')

# Define constraints
const1 = ForAll([j], Implies(And(0 <= j, j<N-1, j % 2 == 0), ss(j) < ss(j+2)))
const2 = ForAll([i], Implies(And(1 <= i, i < N-1, i % 2 != 0), ss(i) < ss(0)))
const3 = Implies(N > 1, ss(N-1) < ss(0))

# Combine the constraints
prediction = And(const1, const2, const3)


########

i = Int('i')
# when N=3, its 0 <= i < 1, ss[0] < ss[2]
# when N=4, its 0 <= i < 2, ss[0] < ss[2], ss[1] < ss[3]
# {ss[i] < ss[i+2] | 0 <= i < N-2} for all i in Z+
# for all i, (0 <= i < N-2) -> (ss[i] < ss[i+2])
truth1 = ForAll([i], Implies(And(0 <= i, i < N-2), ss(i) < ss(i+2)))

# when N=3, ss[1] < ss[0] 
# when N=4, ss[3] < ss[0] 
# {ss[N-1-(N%2)] < ss[0] | 2 <= N}
# (2 <= N) -> (ss[N-1-(N%2)] < ss[0])
truth2 = Implies(2 <= N, ss(N-1-(N%2)) < ss(0))
truth = And(truth1, truth2)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)