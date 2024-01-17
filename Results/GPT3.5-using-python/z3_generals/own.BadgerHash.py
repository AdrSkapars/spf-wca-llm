N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

get0 = Int('get0')
get1 = Int('get1')

# multi-dimensional function
put = Function('put', IntSort(), IntSort(), IntSort())

# for all i, ((0 ≤ i < N) -> put[i, 0] ≠ get0)
predicate1 = ForAll([i], Implies((0 <= i) & (i < N), put(i, 0) != get0))

# (get1 + get0) % N == 0
predicate2 = (get1 + get0) % N == 0

# for all i, ((0 ≤ i < N) -> (put[i, 1] + put[i, 0]) % N == 0)
predicate3 = ForAll([i], Implies((0 <= i) & (i < N), (put(i, 1) + put(i, 0)) % N == 0))

# combine the predicates
prediction = And(predicate1, predicate2, predicate3)
