N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N, N≥3) -> (ss[i] = 45 and ss[i] ≠ 95))
prediction = ForAll([i], Implies(And(0 <= i, i < N, N >= 3), And(ss(i) == 45, ss(i) != 95)))
