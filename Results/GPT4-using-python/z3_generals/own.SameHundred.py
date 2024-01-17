N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 ≤ i < N) -> ss[i] >= 100)
prediction = ForAll([i], Implies(And(1 <= i, i < N), ss(i) >= 100))
