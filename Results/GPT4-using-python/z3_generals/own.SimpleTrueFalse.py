N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, (N - 1 >= i >= 0) -> (ss[i] == (i + 1) % 2)
prediction = ForAll([i], Implies(And(N - 1 >= i, i >= 0), ss(i) == (i + 1) % 2))
