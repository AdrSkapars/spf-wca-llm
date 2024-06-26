from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
j = Int('j')

# for all i, for all j, ((0 ≤ i ≤ j < N),(i = N - j - 1) -> ss[i] < ss[j])
prediction = ForAll([i, j], Implies(And(0 <= i, i < j, j < N, j == N - i-1), ss(i) < ss(j)))


########

i = Int('i')
# when N=2, its 0 <= i < 1, ss[0] < ss[1]
# when N=3, its 0 <= i < 1, ss[0] < ss[2]
# when N=4, its 0 <= i < 2, ss[0] < ss[3], ss[1] < ss[2]
# when N=5, its 0 <= i < 2, ss[0] < ss[4], ss[1] < ss[3]
# {ss[i] < ss[N-i-1] | 0 <= i < (N//2)}
# for all i, (0 <= i < (N//2)) -> (ss[i] < ss[N-i-1])
truth = ForAll([i], Implies(And(0 <= i, i < (N/2)), ss(i) < ss(N-i-1)))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)