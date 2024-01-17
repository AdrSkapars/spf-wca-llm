N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

prediction = ForAll([i], Implies(0 <= i, ss((i+1) % N) < ss(i)))
