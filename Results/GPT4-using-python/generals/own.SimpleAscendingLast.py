
def generate_constraints(N):
    constraints = []
    # Special case for the first constraint
    if N != 1:
        constraints.append(f"in{N-1} < in0")
    # General case for the rest of the constraints
    for i in range(1, N-1):
        constraints.append(f"in{i-1} < in{i}")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
