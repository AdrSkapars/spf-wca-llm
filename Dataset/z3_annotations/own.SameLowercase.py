i = Int('i')
# {97 <= ss[i] <= 122 | 0 <= i < N} for all i in Z+
# for all i, (0 <= i < N) -> (97 <= ss[i] <= 122)
truth = ForAll([i], Implies(And(0 <= i, i < N), And(97 <= ss(i), ss(i) <= 122)))