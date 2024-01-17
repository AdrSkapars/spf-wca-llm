N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
X = Int('X')
K = Int('K')

# for all X and K, ((4 ≤ N, X = 3*K, 3*K < N, K ≥ 1) -> ss[X] = 0)
prediction = ForAll([X, K], Implies(And(4 <= N, X == 3*K, 3*K < N, K >= 1), ss(X) == 0))
