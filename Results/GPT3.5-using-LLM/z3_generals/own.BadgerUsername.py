from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 <= i < N) -> (ss[i] = 45 and ss[i] != 95))
# Use And and Not operators for logical connectives.
prediction1 = ForAll([i], Implies(And(0 <= i, i < N), 
                                  And(ss(i) == 45, ss(i) != 95)))

# If N = 1: {}
# Nothing needs to be defined for this case in the context of z3.
# If N is 1, the previous condition (0 <= i < N) would not hold for any i, because there are no integers i that satisfy 0 <= i < 1.

# Combining the cases.
# Since the second case doesn't introduce any conditions, the prediction is the same as prediction1.
prediction = prediction1 
