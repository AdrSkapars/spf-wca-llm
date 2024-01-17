N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

prediction = ForAll([i], Implies(And(1 <= i, i <= N), ss(i) >= 100))
