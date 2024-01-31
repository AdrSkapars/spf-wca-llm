from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
X = Int('X')
K = Int('K')

# for all X and K, ((4 ≤ N, X = 3*K, 3*K < N, K ≥ 1) -> ss[X] = 0)
prediction = ForAll([X, K], Implies(And(4 <= N, X == 3*K, 3*K < N, K >= 1), ss(X) == 0))


########

i = Int('i')
# {ss[i] == 0 | 1 <= i < N and i%3 == 0} for all i in Z+
# for all i, (1 <= i < N and i%3 == 0) -> (ss[i] == 0)
truth = ForAll([i], Implies(And(1 <= i, i < N, i%3 == 0), ss(i) == 0))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)