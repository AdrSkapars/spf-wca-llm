ss = Function('ss', IntSort(), IntSort(), IntSort())
i = Int('i')
j = Int('j')
# {ss[i,j] == ss[j,i] | 0 <= i <= j < N} for all i, j in Z+
# for all i,j, (0 <= i <= j < N) -> (ss[i,j] == ss[j,i])
truth = ForAll([i,j], Implies(And(0 <= i, i <= j, j < N), ss(i,j) == ss(j,i)))