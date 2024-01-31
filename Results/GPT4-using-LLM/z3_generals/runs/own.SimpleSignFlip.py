from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

# import statements for the z3 module
from z3 import *

# define the variables and function
N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# build up the constraints' pieces
constr1 = ForAll([i], Implies(And(0 <= i, i < N - 1, i % 2 == 0), ss(i) == ss(i+1)))
constr2 = ForAll([i], Implies(And(0 <= i, i < N - 1, i % 2 != 0), ss(i) < ss(i+1)))
constr3 = ForAll([i], Implies(And(0 <= i, i < N - 1, i % 2 == 0), ss(i) < ss(i+1)))
constr4 = ForAll([i], Implies(And(0 <= i, i < N - 1, i % 2 != 0), ss(i) == ss(i+1)))

# combine the constraints into the final specification
prediction_even = And(constr1, constr2)
prediction_odd = And(constr3, constr4)

# the final specification is a disjunction of the two cases
prediction = If(N % 2 == 0, prediction_even, If(N % 2 != 0, prediction_odd, True))


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