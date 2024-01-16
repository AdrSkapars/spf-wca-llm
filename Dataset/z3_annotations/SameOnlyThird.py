# {ss[2] == 0 | 2 < N}
# (2 < N) -> (ss[2] == 0)
truth = Implies(2 < N, ss(2) == 0)