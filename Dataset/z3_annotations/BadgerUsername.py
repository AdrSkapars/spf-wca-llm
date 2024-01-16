i = Int('i')
# {ss[i] == 45 | 0 <= i < N and 3 <= N <= 15} for all i in Z+
# for all i, (0 <= i < N and 3 <= N <= 15) -> (ss[i] == 45)
truth = ForAll([i], Implies(And(0 <= i, i < N, 3 <= N, N <= 15), ss(i) == 45))