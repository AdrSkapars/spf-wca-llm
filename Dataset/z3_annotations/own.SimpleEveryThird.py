i = Int('i')
# {ss[i] == 0 | 1 <= i < N and i%3 == 0} for all i in Z+
# for all i, (1 <= i < N and i%3 == 0) -> (ss[i] == 0)
truth = ForAll([i], Implies(And(1 <= i, i < N, i%3 == 0), ss(i) == 0))