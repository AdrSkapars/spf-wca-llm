N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N-1, i is even) -> ss[i] == ss[i+1]) and ((0 <= i < N-1, i is odd) -> ss[i] < ss[i+1])
prediction = ForAll([i], And(Implies(And(0 <= i, i < N-1, i%2 == 0), ss(i) == ss(i+1)), Implies(And(0 <= i, i < N-1, i%2 == 1), ss(i) < ss(i+1))))
