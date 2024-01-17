N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# Set of constraints for different conditions
s1 = ForAll([i], Implies(And(0 <= i, i < N, i % 2 == 1, N >= 7), And(ss(i) < ss(i-1), ss(i-1) < ss(i-2), ss(i-3) < ss(i-4), ss(1) < ss(0))))
s2 = ForAll([i], Implies(And(0 <= i, i < N, i % 2 == 0, N >= 6), And(ss(i) < ss(i-1), ss(i-1) < ss(i-2), ss(0) < ss(N-2), ss(1) < ss(0))))
s3 = And(ss(3) < ss(2), ss(1) < ss(0), ss(0) < ss(3)) if N == 4 or N == 5 else BoolVal(True)
s4 = ss(1) < ss(0) if N == 2 or N == 3 else BoolVal(True)
s5 = BoolVal(True) if N == 1 else BoolVal(False)

# final specification
prediction = And(s1, s2, s3, s4, s5)
