N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# {in[i-1] = in[i] | 1 ≤ i < (N+2)//2}
specification1 = ForAll([i], Implies(And(1 <= i, i < (N+2)//2), ss(i-1) == ss(i)))

# {in[i-1] < in[i] | (N+2)//2 ≤ i < N}
specification2 = ForAll([i], Implies(And((N+2)//2 <= i, i < N), ss(i-1) < ss(i)))

# for all i, ((1 ≤ i < (N+2)//2) -> ss[i-1] = ss[i]) AND ((N+2)//2 ≤ i < N) -> ss[i-1] < ss[i])
prediction = And(specification1, specification2) 
