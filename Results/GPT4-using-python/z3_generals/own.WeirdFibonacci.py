N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 < i ≤ N-1) -> ss[i] == (ss[i-2] + ss[i-1]))
prediction = ForAll(i, Implies(And(1 < i, i <= N-1), ss(i) == (ss(i-2) + ss(i-1))))
