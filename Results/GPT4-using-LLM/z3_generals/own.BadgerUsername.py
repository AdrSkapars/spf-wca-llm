N = Int('N')
ss = Function('ss', IntSort(), IntSort())
k = Int('k')

definition1 = And(ss(k) == 45, ss(k) != 95)

definitionSet = ForAll([k], Implies(And(0 <= k, k < N), definition1))

prediction = Implies(N > 2, definitionSet)
