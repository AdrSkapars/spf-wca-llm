from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 ≤ i ≤ N-1) -> ss[i] >= 100)
prediction = ForAll([i], Implies(And(1 <= i, i <= N - 1), ss(i) >= 100))


########

i = Int('i')
# {ss[i] >= 100 | 1 <= i < N} for all i in Z+
# for all i, (1 <= i < N) -> (ss[i] >= 100)
truth = ForAll([i], Implies(And(1 <= i, i < N), ss(i) >= 100))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)