
def generate_constraints(N):
    constraints = []

    for i in range(1, N):  # Start loop from 1 as the first input has no constraints
        constraints.append(f"in{i} == (in0 * {i+1})")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
