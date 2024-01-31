from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# Set of constraints for different conditions
s1 = ForAll([i], Implies(And(0 <= i, i < N, i % 2 == 1, N >= 7), And(ss(i) < ss(i-1), ss(i-1) < ss(i-2), ss(i-3) < ss(i-4), ss(1) < ss(0))))
s2 = ForAll([i], Implies(And(0 <= i, i < N, i % 2 == 0, N >= 6), And(ss(i) < ss(i-1), ss(i-1) < ss(i-2), ss(0) < ss(N-2), ss(1) < ss(0))))
s3 = And(ss(3) < ss(2), ss(1) < ss(0), ss(0) < ss(3)) if N == 4 or N == 5 else BoolVal(True)
s4 = ss(1) < ss(0) if N == 2 or N == 3 else BoolVal(True)
s5 = BoolVal(True) if N == 1 else BoolVal(False)

# final specification
prediction = And(s1, s2, s3, s4, s5)


########

i = Int('i')
# {ss[1] < ss[0] | 2 <= N}
# (2 <= N) -> (ss[1] < ss[0])
truth1 = Implies(2 <= N, ss(1) < ss(0))

# when N=4, its 0 <= i <= 1, condition holds for i=0
# when N=5, its 0 <= i <= 1, condition holds for i=0
# when N=6, its 0 <= i <= 3, condition holds for i=0,2
# when N=7, its 0 <= i <= 3, condition holds for i=0,2
# when N=8, its 0 <= i <= 5, condition holds for i=0,2,4
# when N=9, its 0 <= i <= 5, condition holds for i=0,2,4
# {ss[i] < ss[i+3] < ss[i+2] | 0 <= i <= N-(3+N%2) and 4 <= N and i%2 == 0} for all i in Z+
# for all i, (0 <= i <= N-(3+N%2) and 4 <= N and i%2 == 0) -> (ss[i] < ss[i+3] < ss[i+2])
truth2 = ForAll([i], Implies(And(0 <= i, i <= N-(3+N%2), 4 <= N, i%2 == 0), And(ss(i) < ss(i+3), ss(i+3) < ss(i+2))))
truth = And(truth1, truth2)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)