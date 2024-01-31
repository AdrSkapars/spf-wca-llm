from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())

## Index variable declarations
i = Int('i')

## First set as a z3 Predictor
set1 = Implies(N > 1, ss(N-1) < ss(0))

## Second set as a z3 Predictor
set2 = ForAll([i], Implies(And(i >= 1, i < N-1), ss(i-1) < ss(i)))

## Combining the two sets
prediction = And(set1, set2)


########

i = Int('i')
# {ss[i-1] < ss[i] | 1 <= i < N-1} for all i in Z+
# for all i, (1 <= i < N-1) -> (ss[i-1] < ss[i])
truth1 = ForAll([i], Implies(And(1 <= i, i < N-1), ss(i-1) < ss(i)))

# {ss[N-1] < ss[0] | 1 < N} for all i in Z+
# (1 < N) -> (ss[N-1] < ss[0])
truth2 = Implies(1 < N, ss(N-1) < ss(0))
truth = And(truth1, truth2)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)