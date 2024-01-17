N = Int('N')
ss = Function('ss', IntSort(), IntSort())
i = Int('i')

# "No constraints for single input" if N == 1
# "in[i-1] == in[i]" if N == 2
# {in[i] == in[i-1] for 1 ≤ i < (N - ⌊N/2⌋})
# {in[i] < in[i+1] for (N - ⌊N/2⌋) ≤ i < (N - 1)} if 3 ≤ N ≤ 10 for all i ∈ Z+

# for all i, ((1 <= i < (N - ⌊N/2⌋)) -> ss[i] = ss[i-1])
# for all i, (((N - ⌊N/2⌋) <= i < N - 1) -> ss[i] < ss[i+1])
prediction = ForAll([i], 
    Or(
        Implies(And(1 <= i, i < (N - (N/2))), ss(i) == ss(i-1)), 
        Implies(And((N - (N/2)) <= i, i < N - 1), ss(i) < ss(i+1))
    )
)
