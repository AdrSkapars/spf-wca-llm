N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((1 ≤ i < (N+2)//2) -> ss[i-1] == ss[i]) 
# and for all i, (((N+2)//2 ≤ i < N) -> ss[i-1] < ss[i])
prediction = Implies(2 < N, ss(2) == 0)
