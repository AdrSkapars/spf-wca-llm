from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
x = Int('x')

prediction = If(N >= 3, 
                ForAll([x], 
                       Implies(And(0 <= x, x < N), 
                               And(ss(x) == 37, ss(x) != 36, ss(x) != 35, ss(x) != 64)
                              )
                      ),
                True
               )


########

i = Int('i')
# {ss[i] == 37 | 0 <= i < N and 3 <= N <= 10} for all i in Z+
# for all i, (0 <= i < N and 3 <= N <= 10) -> (ss[i] == 37 )
# truth = ForAll([i], Implies(And(0 <= i, i < N, 3 <= N, N <= 10), ss(i) == 37)) # No way of knowing
truth = ForAll([i], Implies(And(0 <= i, i < N, 3 <= N), ss(i) == 37))

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)