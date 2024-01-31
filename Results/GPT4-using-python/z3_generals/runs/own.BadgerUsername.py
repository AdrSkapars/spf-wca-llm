from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N, N≥3) -> (ss[i] = 45 and ss[i] ≠ 95))
prediction = ForAll([i], Implies(And(0 <= i, i < N, N >= 3), And(ss(i) == 45, ss(i) != 95)))


########

i = Int('i')
# {ss[i] == 45 | 0 <= i < N and 3 <= N <= 15} for all i in Z+
# for all i, (0 <= i < N and 3 <= N <= 15) -> (ss[i] == 45)
truth = ForAll([i], Implies(And(0 <= i, i < N, 3 <= N, N <= 15), ss(i) == 45)) # No way of knowing N <= 15
truth = ForAll([i], Implies(And(0 <= i, i < N, 3 <= N), ss(i) == 45))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)