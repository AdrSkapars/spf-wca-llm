N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# preconditions for N not equal to 1
preconditions = Not(N == 1)

# (1 ≤ i < N) -> ss[i] = ss[i-1]
first_set = ForAll([i], Implies(And(1 <= i, i < N), ss(i-1) == ss(i)))

# (1 ≤ i < N-1) -> ss[i] < ss[i+1]
second_set = ForAll([i], Implies(And(1 <= i, i < N-1), ss(i) < ss(i+1)))

# putting it together
prediction = And([preconditions, first_set, second_set])
