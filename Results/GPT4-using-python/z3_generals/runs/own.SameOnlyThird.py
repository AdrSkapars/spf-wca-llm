from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())

# {ss[2] = 0 | N >= 3 }
prediction = Implies(N >= 3, ss(2) == 0)


########

# {ss[2] == 0 | 2 < N}
# (2 < N) -> (ss[2] == 0)
truth = Implies(2 < N, ss(2) == 0)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)