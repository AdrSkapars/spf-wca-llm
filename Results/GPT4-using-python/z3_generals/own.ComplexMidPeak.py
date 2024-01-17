N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# for all i, ((0 <= i < N//2) -> ss[i] < ss[i+1]) and ((N//2 <= i < N-1) -> ss[i] > ss[i+1])
prediction = ForAll([i], Or(
    And(0 <= i, i < N//2, ss(i) < ss(i+1)),
    And(N//2 <= i, i < N-1, ss(i) > ss(i+1)),
))
