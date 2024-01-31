from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((4 divides i < N) -> (ss[i+3] < ss[i+2] and ss[i+1] < ss[i] and ss[i] < ss[i+3]))
prediction_1 = ForAll([i], Implies(And(i % 4 == 0, i < N), And(ss(i + 3) < ss(i + 2), ss(i + 1) < ss(i), ss(i) < ss(i + 3))))

# for all i, ((2 divides i < N and i is not divisible by 4) -> (ss[i+2] < ss[i+1] and ss[i+1] < ss[i+2]))
prediction_2 = ForAll([i], Implies(And(i % 2 == 0, i < N, i % 4 != 0), And(ss(i + 2) < ss(i + 1), ss(i + 1) < ss(i + 2))))

# for all i, ((i+1 < N and i is not divisible by 2) -> (ss[i+1] < ss[i]))
prediction_3 = ForAll([i], Implies(And(i + 1 < N, i % 2 != 0), ss(i + 1) < ss(i)))

# for all i, ((i = 1 mod 4, i+3 < N) -> (ss[i+2] < ss[i+1] and ss[i+1] < ss[i+3]))
prediction_4 = ForAll([i], Implies(And(i % 4 == 1, i + 3 < N), And(ss(i + 2) < ss(i + 1), ss(i + 1) < ss(i + 3))))

# Combine all the predictions
prediction = And(prediction_1, prediction_2, prediction_3, prediction_4)



########

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
truth = And(truth1, truth2)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)