N = Int('N')
ss = Function('ss', IntSort(), IntSort())

# {ss[2] = 0 | N >= 3 }
prediction = Implies(N >= 3, ss(2) == 0)
