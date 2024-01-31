from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort(), IntSort())
i = Int('i')
j = Int('j')

# for all i, for all j, ((0 ≤ j < i < N) -> ss[i,j] == ss[j,i])
prediction = ForAll([i, j], Implies(And(0 <= j, j < i, i < N), ss(i, j) == ss(j, i)))


########

ss = Function('ss', IntSort(), IntSort(), IntSort())
i = Int('i')
j = Int('j')
# {ss[i,j] == ss[j,i] | 0 <= i <= j < N} for all i, j in Z+
# for all i,j, (0 <= i <= j < N) -> (ss[i,j] == ss[j,i])
truth = ForAll([i,j], Implies(And(0 <= i, i <= j, j < N), ss(i,j) == ss(j,i)))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)