N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N-1) -> ss[i] < ss[i+1] and ss[i] == ss[i+1])
prediction = ForAll([i], Implies(And(0 <= i, i < N-1), And(ss(i) < ss(i+1), ss(i) == ss(i+1))))
