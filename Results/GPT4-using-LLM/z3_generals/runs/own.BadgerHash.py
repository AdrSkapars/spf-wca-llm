from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
ss = Function('ss', IntSort(), IntSort())
get = Function('get', IntSort(), IntSort())
put = Function('put', IntSort(), IntSort(), IntSort())
i = Int('i')

# set of constraints 1
constraints1 = ForAll([i], Implies(And(0 <= i, i < N), put(i, 0) != get(0)))

# constraint 2
constraint2 = 0 == ((get(1) + get(0)) % N)

# set of constraints 3
constraints3 = ForAll([i], Implies(And(0 <= i, i < N), 0 == ((put(i, 1) + put(i, 0)) % N)))

# final specification combining all constraints
prediction = And(constraints1, constraint2, constraints3)


########

get = Function('get', IntSort(), IntSort())
put = Function('put', IntSort(), IntSort(), IntSort())

i = Int('i')
# {put[i,0] != get[0] | 0 <= i < N} for all i in Z+
# for all i, (0 <= i < N) -> (put[i,0] != get[0])
truth1 = ForAll([i], Implies(And(0 <= i, i < N), put(i,0) != get(0)))

# {0 == ((get[1] + get[0]) % N)}
# 0 == ((get[1] + get[0]) % N)
truth2 = 0 == ((get(1) + get(0)) % N)

# {0 == ((put[i,1] + put[i,0]) % N) | 0 <= i < N} for all i in Z+
# for all i, (0 <= i < N) -> (0 == (put[i,1] + put[i,0]) % N))
truth3 = ForAll([i], Implies(And(0 <= i, i < N), (0 == (put(i,1) + put(i,0)) % N)))
truth = And(truth1, truth2, truth3)

########

prove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)