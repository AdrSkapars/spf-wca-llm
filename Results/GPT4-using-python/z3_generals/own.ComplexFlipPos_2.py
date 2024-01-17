N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')
j = Int('j')

# 'in_[i] < in_[i-1]' constraints
pred1 = ForAll([i], Implies(And(i > 0, i <= (N-1), i%2==1), ss(i) < ss(i-1)))

# 'in_0 < in_[i]' constraints
pred2 = ForAll([i], Implies(And(i > 2, i <= (N-1), i%2==1), ss(0) < ss(i)))

# 'in1 < in0' constraint
pred3 = Implies(N > 1, ss(1) < ss(0))

# 'in_[i-2] < in_[i]' constraints
pred4 = ForAll([i], Implies(And(i >= 4, i < N, i%2==0), ss(i-2) < ss(i)))

prediction = And(pred1, pred2, pred3, pred4)
