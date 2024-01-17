N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 <= i < N) -> 97 <= ss[i] <= 122)
prediction = ForAll(i, Implies(0 <= i, i < N, And(97 <= ss(i), ss(i) <= 122)))
