from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((3 <= i <= N, i mod 3 == 0) -> ss[i] == 0)
prediction = ForAll([i], Implies(And(3 <= i, i <= N, i < N, i % 3 == 0), ss(i) == 0))


########

i = Int('i')
# {ss[i] == 0 | 1 <= i < N and i%3 == 0} for all i in Z+
# for all i, (1 <= i < N and i%3 == 0) -> (ss[i] == 0)
truth = ForAll([i], Implies(And(1 <= i, i < N, i%3 == 0), ss(i) == 0))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)