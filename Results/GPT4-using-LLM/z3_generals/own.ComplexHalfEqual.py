N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < 2 ∨ N-4 ≤ i < N) -> ss[i] == ss[i+1]) ∪ ((2 ≤ i < N-4) -> ss[i] < ss[i+1])
prediction = ForAll([i], Or(
    Implies(Or(And(0 <= i, i < 2), And(N-4 <= i, i < N)), ss(i) == ss(i+1)),
    Implies(And(2 <= i, i < N-4), ss(i) < ss(i+1))
))
