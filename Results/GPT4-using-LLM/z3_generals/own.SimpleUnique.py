N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# {in[i-1] = in[i]  |  1 ≤ i < (N+2)//2}
pred1 = ForAll([i], Implies(And(1 <= i, i < (N+2)//2), ss(i-1) == ss(i)))

# {in[i-1] < in[i]  |  (N+2)//2 ≤ i < N} for all i ∈ Z+
pred2 = ForAll([i], Implies(And((N+2)//2 <= i, i < N), ss(i-1) < ss(i)))

# combine the predictions
prediction = And(pred1, pred2)
