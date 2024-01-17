N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N) -> (ss[i] == 45 and ss[i] != 95)) if N > 2
prediction = ForAll([i], If(N > 2, And(0<=i, i<N, ss(i)==45, ss(i)!=95), True))
