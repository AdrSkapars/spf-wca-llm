from z3 import *

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# ss[i] < ss[i - 1], for i = 1 and i = 0
constraints1 = ForAll([i], And(i == 1, ss(i) < ss(i - 1))) 
constraints2 = ForAll([i], And(i == 0, ss(i) < ss(3)))

# ss[N - 1] < ss[N - 2], for N >= 4
constraints3 = ForAll([N], Implies( N >= 4, ss(N - 1) < ss(N - 2)))

# ss[N - 3] < ss[N - 4], for N not a multiple of 4 and N >= 5
constraints4 = ForAll([N], Implies(And(N % 4 != 0, N >= 5), ss(N - 3) < ss(N - 4)))

# ss[N - 2] < ss[N - 1], if N is a multiple of 4
# ss[N - 2] < ss[N - 3], if N is not a multiple of 4
# for all N >= 5
constraints5 = ForAll([N], Implies(N >= 5,
                                    If(N % 4 == 0, ss(N - 2) < ss(N - 1), ss(N - 2) < ss(N - 3))))

# Final specification
prediction = And(constraints1, constraints2, constraints3, constraints4, constraints5)
