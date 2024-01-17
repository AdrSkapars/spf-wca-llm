N = Int('N')
ss = Function('ss', IntSort(), IntSort(), IntSort())
i = Int('i')
j = Int('j')

# {in[j]x[i] = in[i]x[j] | 0 ≤ i < j < N} for all i, j ∈ Z+
prediction = ForAll([i, j], Implies(And(0 <= i, i < j, j < N), ss(j, i) == ss(i, j)))
