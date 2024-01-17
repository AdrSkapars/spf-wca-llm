N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# in[i-1] = in[i] for 1 ≤ i < (N+2)//2
first_half_pred = ForAll([i], Implies(And(1 <= i, i < (N+2)//2), ss(i-1) == ss(i)))

# in[i-1] < in[i] for (N+2)//2 ≤ i < N
second_half_pred = ForAll([i], Implies(And((N+2)//2 <= i, i < N), ss(i-1) < ss(i)))

# Combine both halves with union operation
prediction = And(first_half_pred, second_half_pred)
