from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
j = Int('j')

# Floor and ceiling functions using z3 Div and Mod
floor_div = lambda x,y: (x/ y)
ceiling_div = lambda x,y: If(x % y == 0, (x/ y), (x/ y) + 1)

# If-then-else expressions for the specific conditions
condition1 = And(0 <= i, i < j, j < N)
condition2 = And(0 <= i, i <= floor_div(N, 2) - 1, ceiling_div(N, 2) + i == j)
condition3 = And(N == 1)

# ForAll expressions for each condition
expr1 = ForAll([i, j], Implies(condition1, ss(i) < ss(j)))
expr2 = ForAll([i, j], Implies(condition2, ss(i) < ss(j)))
expr3 = ForAll([i, j], Implies(condition3, ss(i) == ss(j)))

# Final prediction combining all expressions
prediction = And(expr1, expr2, expr3)


########

i = Int('i')
# when N=2, its 0 <= i < 1, ss[0] < ss[1]
# when N=3, its 0 <= i < 1, ss[0] < ss[2]
# when N=4, its 0 <= i < 2, ss[0] < ss[3], ss[1] < ss[2]
# when N=5, its 0 <= i < 2, ss[0] < ss[4], ss[1] < ss[3]
# {ss[i] < ss[N-i-1] | 0 <= i < (N//2)}
# for all i, (0 <= i < (N//2)) -> (ss[i] < ss[N-i-1])
truth = ForAll([i], Implies(And(0 <= i, i < (N/2)), ss(i) < ss(N-i-1)))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)