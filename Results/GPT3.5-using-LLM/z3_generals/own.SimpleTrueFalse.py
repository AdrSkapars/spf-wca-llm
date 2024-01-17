N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N) -> ss[i] == (i+1) mod 2)
prediction = ForAll(i, Implies(0 <= i < N, ss(i) == (i+1) % 2))
