N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
j = Int('j')

prediction = ForAll([i, j], Implies(And(0 <= i, i < j, j < N), ss(i) != ss(j)))
