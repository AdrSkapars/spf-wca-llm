N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 <= i < N//2) -> ss[i] < ss[i+1]) and ((N//2 <= i < N-1) -> ss[i] > ss[i+1])
prediction1 = ForAll([i], Implies(And(0 <= i, i < N/2), ss(i) < ss(i+1)))
prediction2 = ForAll([i], Implies(And(N/2 <= i, i < N-1), ss(i) > ss(i+1)))
prediction = And(prediction2, prediction1)