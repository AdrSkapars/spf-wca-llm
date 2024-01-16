i = Int('i')
# when N=3, its 0 <= i < 1, ss[0] < ss[2]
# when N=4, its 0 <= i < 2, ss[0] < ss[2], ss[1] < ss[3]
# {ss[i] < ss[i+2] | 0 <= i < N-2} for all i in Z+
# for all i, (0 <= i < N-2) -> (ss[i] < ss[i+2])
truth1 = ForAll([i], Implies(And(0 <= i < N-2), ss(i) < ss(i+2)))

# when N=3, ss[1] < ss[0] 
# when N=4, ss[3] < ss[0] 
# {ss[N-1-(N%2)] < ss[0] | 2 <= N}
# (2 <= N) -> (ss[N-1-(N%2)] < ss[0])
truth2 = Implies(2 <= N, ss(N-1-(N%2)) < ss(0))
truth = And(truth1, truth2)