i = Int('i')
# when N=2, its 2 <= i <= 2, ss[1] == 2*ss[0]
# when N=3, its 2 <= i <= 3, ss[1] == 2*ss[0],  ss[2] == 3*ss[0]
# {ss[i-1] == i*ss[0] | 2 <= i <= N} for all i in Z+
# for all i, (2 <= i <= N) -> (ss[i-1] == i*ss[0])
truth = ForAll([i], Implies(And(2 <= i, i <= N), ss(i-1) == i*ss(0))