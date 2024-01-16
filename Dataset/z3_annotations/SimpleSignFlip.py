i = Int('i')
# {ss[i-1] == ss[i] | 1 <= i < N and i%2 == 1} for all i in Z+
# for all i, (1 <= i < N and i%2 == 1) -> (ss[i-1] == ss[i])
truth1 = ForAll([i], Implies(And(1 <= i, i < N, i%2 == 1), ss(i-1) == ss(i)))
# {ss[i-1] < ss[i] | 1 <= i < N and i%2 == 0} for all i in Z+
# for all i, (1 <= i < N and i%2 == 0) -> (ss[i-1] < ss[i])
truth2 = ForAll([i], Implies(And(1 <= i, i < N, i%2 == 0), ss(i-1) < ss(i)))
truth = And(truth1, truth2)