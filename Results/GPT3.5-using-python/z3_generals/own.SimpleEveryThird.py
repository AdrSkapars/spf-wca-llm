N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

pattern1 = ForAll([i], Implies(And(1 <= i, i < (N+2)//2), ss(i-1) == ss(i)))
pattern2 = ForAll([i], Implies(And((N+2)//2 <= i, i < N), ss(i-1) < ss(i)))

prediction = And(pattern1, pattern2)
