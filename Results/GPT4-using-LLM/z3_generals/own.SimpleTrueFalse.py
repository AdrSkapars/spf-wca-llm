N = Int('N')
ss = Function('ss', IntSort(), IntSort())
X = Int('X')

# for all X, (0 ≤ X < N) -> ss[X] = 1 - (X mod 2)
prediction = ForAll([X], Implies(And(0 <= X, X < N), ss(X) == 1 - (X % 2)))
