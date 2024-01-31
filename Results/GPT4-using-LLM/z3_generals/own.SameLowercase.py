N = Int('N')
ss = Function('ss', IntSort(), IntSort())
X = Int('X')

# for all X, (0 ≤ X < N -> (97 ≤ ss[X] ≤ 122))
prediction = ForAll([X], Implies(And(0 <= X, X < N), And(97 <= ss(X), ss(X) <= 122)))
