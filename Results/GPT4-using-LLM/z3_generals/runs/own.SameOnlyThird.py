from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 ≤ i < (N+2)//2) -> ss[i-1] == ss[i]) 
# and for all i, (((N+2)//2 ≤ i < N) -> ss[i-1] < ss[i])
prediction = Implies(2 < N, ss(2) == 0)


########

# {ss[2] == 0 | 2 < N}
# (2 < N) -> (ss[2] == 0)
truth = Implies(2 < N, ss(2) == 0)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)