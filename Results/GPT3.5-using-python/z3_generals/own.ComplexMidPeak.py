N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, if (0 ≤ i < N-1 and i is even) then (ss[i+1] > ss[i]) and if (0 ≤ i < N-1 and i is odd) then (ss[i] < ss[i+1])
prediction = ForAll([i], Implies(And(0 <= i, i < N-1), If(i % 2 == 0, ss(i+1) > ss(i), ss(i) < ss(i+1))))
