N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
j = Int('j')

# for all i, for all j, ((0 ≤ j < i < N) -> (ss(i)*ss(j) = ss(j)*ss(i)))
prediction = ForAll([i, j], Implies(And(0 <= j, j < i, i < N), ss(i)*ss(j) == ss(j)*ss(i)))
