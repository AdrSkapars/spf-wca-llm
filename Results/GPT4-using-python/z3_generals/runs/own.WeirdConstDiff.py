from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((2 ≤ i < N) -> (ss[i] - ss[i-1]) == (ss[i-1] - ss[i-2]))
prediction = ForAll([i], Implies(And(2 <= i, i < N), (ss(i) - ss(i-1)) == (ss(i-1) - ss(i-2))))


########

i = Int('i')
# when N=3, its 2 <= i < 3, ss[1]-ss[0] == ss[2]-ss[1]
# {ss[i-1]-ss[i-2] == ss[i]-ss[i-1] | 2 <= i < N} for all i in Z+
# for all i, (2 <= i < N) -> (ss[i-1]-ss[i-2] == ss[i]-ss[i-1])
truth = ForAll([i], Implies(And(2 <= i, i < N), ss(i-1)-ss(i-2) == ss(i)-ss(i-1)))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)