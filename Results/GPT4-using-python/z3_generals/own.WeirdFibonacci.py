N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((3 ≤ i ≤ N) -> ss[i] == (ss[i-2] + ss[i-1]))
prediction = ForAll(i, Implies(And(3 <= i, i <= N), ss(i) == (ss(i-2) + ss(i-1))))
