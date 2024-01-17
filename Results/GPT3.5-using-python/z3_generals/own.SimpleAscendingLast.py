N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 ≤ i < N) -> And(ss[i] < ss[0], ss[0] < ss[i]))
prediction = ForAll([i], Implies(And(1 <= i, i < N), And(ss(i) < ss(0), ss(0) < ss(i))))
