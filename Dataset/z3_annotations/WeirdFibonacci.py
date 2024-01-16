i = Int('i')
# {ss[i-2]+ss[i-1] == ss[i] | 2 <= i < N} for all i in Z+
# for all i, (2 <= i < N) -> (ss[i-2]+ss[i-1] == ss[i])
truth = ForAll([i], Implies(And(2 <= i, i < N), ss(i-2)+ss(i-1) == ss(i)))