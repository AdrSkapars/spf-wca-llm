N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N) -> ss(i) = 1 - (i mod 2))
prediction = ForAll([i], Implies(0 <= i < N, ss(i) == 1 - (i % 2)))
