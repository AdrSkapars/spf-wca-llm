from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < ⌊N/2⌋) -> ss[i] < ss[N-i-1])
prediction = ForAll([i], Implies(And(0 <= i, i < N / 2), ss(i) < ss(N - i - 1)))
