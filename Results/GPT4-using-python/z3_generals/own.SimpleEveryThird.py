N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((3 <= i <= N, i mod 3 == 0) -> ss[i] == 0)
prediction = ForAll([i], Implies(And(3 <= i, i <= N, i % 3 == 0), ss(i) == 0))
