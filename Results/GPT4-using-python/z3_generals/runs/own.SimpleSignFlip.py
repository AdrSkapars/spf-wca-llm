from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < N-1, i is even) -> ss[i] == ss[i+1]) and ((0 <= i < N-1, i is odd) -> ss[i] < ss[i+1])
prediction = ForAll([i], And(Implies(And(0 <= i, i < N-1, i%2 == 0), ss(i) == ss(i+1)), Implies(And(0 <= i, i < N-1, i%2 == 1), ss(i) < ss(i+1))))


########

i = Int('i')
# {ss[i-1] == ss[i] | 1 <= i < N and i%2 == 1} for all i in Z+
# for all i, (1 <= i < N and i%2 == 1) -> (ss[i-1] == ss[i])
truth1 = ForAll([i], Implies(And(1 <= i, i < N, i%2 == 1), ss(i-1) == ss(i)))
# {ss[i-1] < ss[i] | 1 <= i < N and i%2 == 0} for all i in Z+
# for all i, (1 <= i < N and i%2 == 0) -> (ss[i-1] < ss[i])
truth2 = ForAll([i], Implies(And(1 <= i, i < N, i%2 == 0), ss(i-1) < ss(i)))
truth = And(truth1, truth2)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)