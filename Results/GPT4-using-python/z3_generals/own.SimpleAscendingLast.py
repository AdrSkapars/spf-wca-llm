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
