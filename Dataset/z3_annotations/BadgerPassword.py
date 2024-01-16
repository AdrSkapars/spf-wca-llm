i = Int('i')
# {ss[i] == 37 | 0 <= i < N and 3 <= N <= 10} for all i in Z+
# for all i, (0 <= i < N and 3 <= N <= 10) -> (ss[i] == 37 )
truth = ForAll([i], Implies(And(0 <= i, i < N, 3 <= N, N <= 10), ss(i) == 37))