N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 ≤ i < (N+2)//2) -> ss[i-1] == ss[i]) 
# and for all i, (((N+2)//2 ≤ i < N) -> ss[i-1] < ss[i])
prediction = ForAll(i, And(
    Implies(And(1 <= i, i < (N+2)//2), ss(i-1) == ss(i)),
    Implies(And((N+2)//2 <= i, i < N), ss(i-1) < ss(i))
))
