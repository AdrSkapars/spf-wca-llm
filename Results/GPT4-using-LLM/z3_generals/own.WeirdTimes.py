N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 ≤ i < N) -> ss[i] == ss[0] * (i+1)), for N > 1
prediction = ForAll(i, Implies(And(N > 1, 1 <= i, i < N), ss(i) == ss(0) * (i+1)))
