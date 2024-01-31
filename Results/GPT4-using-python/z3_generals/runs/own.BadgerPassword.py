from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 <= i < N) -> (ss[i] == 37 And ss[i] != 36 And ss[i] != 35 And ss[i] != 64)), N > 2
prediction = ForAll([i], Implies(And(0 <= i, i < N, N > 2), And(ss(i) == 37, ss(i) != 36, ss(i) != 35, ss(i) != 64)))


########

i = Int('i')
# {ss[i] == 37 | 0 <= i < N and 3 <= N <= 10} for all i in Z+
# for all i, (0 <= i < N and 3 <= N <= 10) -> (ss[i] == 37 )
# truth = ForAll([i], Implies(And(0 <= i, i < N, 3 <= N, N <= 10), ss(i) == 37)) # No way of knowing
truth = ForAll([i], Implies(And(0 <= i, i < N, 3 <= N), ss(i) == 37))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)