from z3 import *
N = Int('N')
ss = Function('ss', IntSort(), IntSort())

########

N = Int('N')
i = Int('i')
get = Function('get', IntSort(), IntSort())
put = Function('put', IntSort(), IntSort(), IntSort())

# put[N-i-1]_0 ≠ get0 | for all i ∈ Z+ where 0 ≤ i < N,
constraint1 = ForAll([i], Implies(And(0 <= i, i < N), put(N-i-1, 0) != get(0)))

# 0 == ((put[N-i-1]_1 + put[N-i-1]_0) % N) | for all i ∈ Z+ where 0 ≤ i < N,
constraint2 = ForAll([i], Implies(And(0 <= i, i < N), 0 == ((put(N-i-1, 1) + put(N-i-1, 0)) % N)))

# 0 == ((get1 + get0) % N)
constraint3 = 0 == ((get(1) + get(0)) % N)

prediction = And(constraint1, constraint2, constraint3)


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