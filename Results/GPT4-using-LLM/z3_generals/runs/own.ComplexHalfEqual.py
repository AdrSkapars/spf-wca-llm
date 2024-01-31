from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 ≤ i < 2 ∨ N-4 ≤ i < N) -> ss[i] == ss[i+1]) ∪ ((2 ≤ i < N-4) -> ss[i] < ss[i+1])
prediction = ForAll([i], Or(
    Implies(Or(And(0 <= i, i < 2), And(N-4 <= i, i < N)), ss(i) == ss(i+1)),
    Implies(And(2 <= i, i < N-4), ss(i) < ss(i+1))
))


########

i = Int('i')
# when N=3, its 1 <= i < 2, ss[0] == ss[1]
# when N=4, its 1 <= i < 3, ss[0] == ss[1] == ss[2]
# {ss[i-1] == ss[i] for 1 <= i < ((N+2)//2)}
# for all i, (1 ≤ i ((N+2)//2) -> (ss[i-1] == ss[i])
truth1 = ForAll([i], Implies(And(1 <= i, i < ((N+2)/2)), ss(i-1) == ss(i)))

# when N=3, its 2 <= i < 3, ss[1] < ss[2]
# when N=4, its 3 <= i < 4, ss[2] < ss[3]
# {ss[i-1] < ss[i] | ((N+2)//2) <= i < N}
# for all i, ((N+2)//2) <= i < N) -> (ss[i-1] < ss[i])
truth2 = ForAll([i], Implies(And(((N+2)/2) <= i, i < N), ss(i-1) < ss(i)))
truth = And(truth1, truth2)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)