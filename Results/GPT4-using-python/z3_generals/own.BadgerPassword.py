N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 <= i < N) -> (ss[i] == 37 And ss[i] != 36 And ss[i] != 35 And ss[i] != 64)), N > 2
prediction = ForAll([i], Implies(And(0 <= i, i < N), And(ss(i) == 37, ss(i) != 36, ss(i) != 35, ss(i) != 64)), N > 2)
