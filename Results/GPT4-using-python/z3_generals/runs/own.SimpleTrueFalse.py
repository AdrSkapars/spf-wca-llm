from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, (N - 1 >= i >= 0) -> (ss[i] == (i + 1) % 2)
prediction = ForAll([i], Implies(And(N - 1 >= i, i >= 0), ss(i) == (i + 1) % 2))


########

i = Int('i')
# {ss[i] == 1-(i%2) | 0 <= i < N} for all i in Z+
# for all i, (0 <= i < N) -> (ss[i] == 1-(i%2))
truth = ForAll([i], Implies(And(0 <= i, i < N), ss(i) == 1-(i%2)))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)