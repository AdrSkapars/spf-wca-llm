N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((2 <= i < N) -> ss[i] == ss[i-2] + ss[i-1])
prediction = ForAll(i, Implies(And(2 <= i, i < N), ss(i) == ss(i-2) + ss(i-1)))
