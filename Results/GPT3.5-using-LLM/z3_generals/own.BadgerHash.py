N = Int('N')
ss = Function('ss', IntSort(), IntSort())
put = Function('put', IntSort(), IntSort())
get = Function('get', IntSort(), IntSort())
i = Int('i')
j = Int('j')

# for all i, for all j, ((0 ≤ i ≠ j < N) -> (put[i] % get[j] == 0 and put[i] > get[j]))
prediction = ForAll([i, j], Implies(And(0 <= i, i != j, j < N), And(put(i) % get(j) == 0, put(i) > get(j))))
