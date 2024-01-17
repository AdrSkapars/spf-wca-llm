from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
j = Int('j')
i = Int('i')

# for all i, for all j, ((0 ≤ j < i < N) -> ss[j] < ss[i])
prediction = ForAll([i, j], Implies(And(0 <= j, j < i, i < N), ss(j) < ss(i)))
