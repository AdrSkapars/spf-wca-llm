from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, (0 ≤ i < N) -> (ss[i] = 37 ∧ ss[i] ≠ 36 ∧ ss[i] ≠ 35 ∧ ss[i] ≠ 64)
first_prediction = ForAll([i], Implies(And(0 <= i, i < N, N > 1), 
                                         And(ss(i) == 37, ss(i) != 36, ss(i) != 35, ss(i) != 64)))

# for all i, (1 ≤ i < N) -> (ss[i] = 37 ∧ ss[i] ≠ 36 ∧ ss[i] ≠ 35 ∧ ss[i] ≠ 64 ∧ ss[i-1] = 37 ∧ ss[i-1] ≠ 36 ∧ ss[i-1] ≠ 35 ∧ ss[i-1] ≠ 64)
second_prediction = ForAll([i], Implies(And(1 <= i, i < N, N > 1), 
                                          And(ss(i) == 37, ss(i) != 36, ss(i) != 35, ss(i) != 64, ss(i-1) == 37, ss(i-1) != 36, ss(i-1) != 35, ss(i-1) != 64)))

# Final prediction
prediction = And(first_prediction, second_prediction)
