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