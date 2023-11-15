
def generate_constraints(N):
    constraints = []
    for i in range(N):
        next_index = (i + 1) % N
        constraints.append(f"in{next_index} < in{i}")
    return constraints
