i = Int('i')
# {ss[i-1] < ss[i] | 1 <= i < N-1} for all i in Z+
# for all i, (1 <= i < N-1) -> (ss[i-1] < ss[i])
truth1 = ForAll([i], Implies(And(1 <= i, i < N-1), ss(i-1) < ss(i)))

# {ss[N-1] < ss[0] | 2 < N} for all i in Z+
# (1 < N) -> (ss[N-1] < ss[0])
truth2 = Implies(2 < N, ss(N-1) < ss(0))
truth = And(truth1, truth2)