N = Int('N')
ss = Function('ss', IntSort(), IntSort())
k = Int('k')

# for all k, ((1 ≤ k < N) -> ss[N-k] = ss[0] * (N-k+1))
prediction = ForAll([k], Implies(And(1 <= k, k < N), ss(N-k) == ss(0)*(N-k+1)))
