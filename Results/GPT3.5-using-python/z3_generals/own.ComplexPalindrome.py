N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 <= i < N-1) -> ss[i] < ss[i+1]) and 
#             ((i < N-2) -> ss[i] < ss[i+2])
prediction = ForAll(i, And(
    Implies(And(0 <= i, i < N-1), ss(i) < ss(i+1)),
    Implies(i < N-2, ss(i) < ss(i+2))))
