N = Int('N')
ss = Function('ss', IntSort(), IntSort())
k = Int('k')

# for all k, ((2 ≤ k < N) -> ss[k] = ss[k-2] + ss[k-1])
prediction = ForAll(k, Implies(And(2 <= k, k < N), ss(k) == ss(k-2) + ss(k-1))) 
