from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, (0 ≤ i < N -> ss[i] = 120)
prediction = ForAll([i], Implies(And(0 <= i, i < N), ss(i) == 120))


########

i = Int('i')
# {ss[i] == 120 | 0 <= i < N} for all i in Z+
# for all i, (0 <= i < N) -> (ss[i] == 120)
truth = ForAll([i], Implies(And(0 <= i, i < N), ss(i) == 120))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)