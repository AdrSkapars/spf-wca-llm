i = Int('i')
# {ss[i] >= 100 | 1 <= i < N} for all i in Z+
# for all i, (1 <= i < N) -> (ss[i] >= 100)
truth = ForAll([i], Implies(And(1 <= i, i < N), ss(i) >= 100))