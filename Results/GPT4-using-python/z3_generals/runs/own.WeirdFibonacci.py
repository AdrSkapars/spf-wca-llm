from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 < i ≤ N-1) -> ss[i] == (ss[i-2] + ss[i-1]))
prediction = ForAll(i, Implies(And(1 < i, i <= N-1), ss(i) == (ss(i-2) + ss(i-1))))


########

i = Int('i')
# {ss[i-2]+ss[i-1] == ss[i] | 2 <= i < N} for all i in Z+
# for all i, (2 <= i < N) -> (ss[i-2]+ss[i-1] == ss[i])
truth = ForAll([i], Implies(And(2 <= i, i < N), ss(i-2)+ss(i-1) == ss(i)))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)