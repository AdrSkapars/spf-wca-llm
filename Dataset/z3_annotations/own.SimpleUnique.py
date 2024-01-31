i = Int('i')
j = Int('j')
# {ss[i] != ss[j] | 0 <= i < j < N} for all i, j in Z+
# for all i and j, (0 <= i < j < N) -> (ss[i] != ss[j])
truth = ForAll([i, j], Implies(And(0 <= i, i < j, j < N), ss(i) != ss(j)))