from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

from z3 import *

# Define N and ss as before
N = Int('N')
ss = Function('ss', IntSort(), IntSort())
M = Int('M')

# Define i, j, and k 
i = Int('i')
j = Int('j')
k = Int('k')

# Define constraints
M_def = M == (N/2)

set1 = ForAll(i, Implies(And(0 <= i, i < M, i + 1 < N), ss(i) > ss(i + 1)))
set2 = ForAll(j, Implies(And(M <= j, j < N, j + 1 < N, (j-M) % 2 == 0), ss(j) > ss(j + 1)))
set3 = ForAll(k, Implies(And(M <= k, k < N, k + 1 < N, (k-M) % 2 == 1), ss(k) < ss(k + 1)))

# Combine all constraints
prediction = And(M_def, set1, set2, set3)


########

i = Int('i')
# when N=3, its 1 <= i < 2, ss[0] < ss[1]
# when N=4, its 1 <= i < 3, ss[0] < ss[1] < ss[2]
# {ss[i-1] < ss[i] | 1 <= i < ((N+2)//2)}
# for all i, (1 ≤ i ((N+2)//2) -> (ss[i-1] < ss[i])
truth1 = ForAll([i], Implies(And(1 <= i, i < ((N+2)/2)), ss(i-1) < ss(i)))

# when N=3, its 2 <= i < 3, ss[1] > ss[2]
# when N=4, its 3 <= i < 4, ss[2] > ss[3]
# {ss[i-1] > ss[i] | ((N+2)//2) <= i < N}
# for all i, ((N+2)//2) <= i < N) -> (ss[i-1] > ss[i])
truth2 = ForAll([i], Implies(And(((N+2)/2) <= i, i < N), ss(i-1) > ss(i)))
truth = And(truth1, truth2)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)