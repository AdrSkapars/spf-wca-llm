i = Int('i')
# {ss[i] == 1-(i%2) | 0 <= i < N} for all i in Z+
# for all i, (0 <= i < N) -> (ss[i] == 1-(i%2))
truth = ForAll([i], Implies(And(0 <= i, i < N), ss[i] == 1-(i%2)))