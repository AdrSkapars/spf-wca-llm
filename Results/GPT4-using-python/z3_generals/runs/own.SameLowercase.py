from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N) -> (97 ≤ ss[i] ≤ 122))
prediction = ForAll([i], Implies(And(0 <= i, i < N), And(ss(i) >= 97, ss(i) <= 122)))


########

i = Int('i')
# {97 <= ss[i] <= 122 | 0 <= i < N} for all i in Z+
# for all i, (0 <= i < N) -> (97 <= ss[i] <= 122)
truth = ForAll([i], Implies(And(0 <= i, i < N), And(97 <= ss(i), ss(i) <= 122)))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)