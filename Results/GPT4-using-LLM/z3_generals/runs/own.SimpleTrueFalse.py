from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
X = Int('X')

# for all X, (0 ≤ X < N) -> ss[X] = 1 - (X mod 2)
prediction = ForAll([X], Implies(And(0 <= X, X < N), ss(X) == 1 - (X % 2)))


########

i = Int('i')
# {ss[i] == 1-(i%2) | 0 <= i < N} for all i in Z+
# for all i, (0 <= i < N) -> (ss[i] == 1-(i%2))
truth = ForAll([i], Implies(And(0 <= i, i < N), ss(i) == 1-(i%2)))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)