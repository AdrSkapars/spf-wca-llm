N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# For N = 2, {in1 < in0}
constraint1 = Implies(N == 2, ss(1) < ss(0))

# For N = 3, {in0 < in2, in1 < in0}
constraint2 = Implies(N == 3, And(ss(0) < ss(2), ss(1) < ss(0)))

# For N ≥ 4, the system includes: {in[i] < in[i+2] | 0 ≤ i ≤ N-3}
constraint3 = ForAll([i], Implies(And(N >= 4, 0 <= i, i <= N-3), ss(i) < ss(i+2)))

# For N ≥4, the system includes: {in[N - (4 - N%2)] < in0}
constraint4 = Implies(N >= 4, ss(N - (4 - N%2)) < ss(0))

# The final prediction
prediction = And(constraint1, constraint2, constraint3, constraint4)
