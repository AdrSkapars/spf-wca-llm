N = Int('N')
ss = Function('ss', IntSort(), IntSort())

# If N > 2, ss[2] == 0
prediction = Implies(N > 2, ss(2) == 0)
