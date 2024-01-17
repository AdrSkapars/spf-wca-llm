N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i ≤ (N-2)/2) -> ss[N-1-i] < ss[i])
prediction = ForAll([i], Implies(And(0 <= i, i <= (N-2)/2), ss(N-1-i) < ss(i)))
