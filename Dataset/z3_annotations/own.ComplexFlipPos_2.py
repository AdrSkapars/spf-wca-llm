i = Int('i')
# {ss[1] < ss[0] | 2 <= N}
# (2 <= N) -> (ss[1] < ss[0])
truth1 = Implies(2 <= N, ss(1) < ss(0))

# when N=4, its 0 <= i <= 1, condition holds for i=0
# when N=5, its 0 <= i <= 1, condition holds for i=0
# when N=6, its 0 <= i <= 3, condition holds for i=0,2
# when N=7, its 0 <= i <= 3, condition holds for i=0,2
# when N=8, its 0 <= i <= 5, condition holds for i=0,2,4
# when N=9, its 0 <= i <= 5, condition holds for i=0,2,4
# {ss[i] < ss[i+3] < ss[i+2] | 0 <= i <= N-(3+N%2) and 4 <= N and i%2 == 0} for all i in Z+
# for all i, (0 <= i <= N-(3+N%2) and 4 <= N and i%2 == 0) -> (ss[i] < ss[i+3] < ss[i+2])
truth2 = ForAll([i], Implies(And(0 <= i, i <= N-(3+N%2), 4 <= N, i%2 == 0), And(ss(i) < ss(i+3), ss(i+3) < ss(i+2))))

# {ss[N-3] < ss[N-1] | 3 <= N and N%2 == 1}
# (3 <= N and N%2 == 1) -> (ss[N-3] < ss[N-1])
truth3 = Implies(And(3 <= N, N%2 == 1), ss(N-3) < ss(N-1))
truth = And(truth1, truth2, truth3)