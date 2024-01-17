N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N) -> (ss[i] ≤ 122 and ss[i] ≥ 97))
prediction = ForAll([i], Implies(0 <= i < N, And(ss(i) <= 122, ss(i) >= 97)))
