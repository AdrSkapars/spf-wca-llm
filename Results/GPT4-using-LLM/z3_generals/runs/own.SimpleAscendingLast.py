from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
j = Int('j')

# The constraints are divided into two parts, i.e., the two sets in the union,
# and are handled separately due to their different conditions for N and i.

# Constraints for in[N-1] < in[0]
constraint1 = ForAll([N], Implies(N > 0, ss(N-1) < ss(0)))

# Constraints for increments of in[i] with a changing decrement step
constraint2 = ForAll(
    [i, j, N],
    Implies(
        And(
            N > 4,
            0 <= i,
            i < j,
            j < N,
            j == i + 1,
            Not(i % 2 == 0)  # i runs in steps of -2
        ),
        ss(i) < ss(j)
    )
)

constraint3 = ForAll(
    [i, j, N],
    Implies(
        And(
            Or(N <= 4, i % 2 == 0),  # i running in steps of -1
            0 <= i,
            i < j,
            j < N,
            j == i + 1,
            Or(
                And(N == 3, i == (N - 1) / 2),
                And(N == 4, i == N / 2)
            )
        ),
        ss(i) < ss(j)
    )
)

# combining the three constraints
prediction = And(constraint1, constraint2, constraint3)


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