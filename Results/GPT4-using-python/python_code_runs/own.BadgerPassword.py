
def generate_constraints(N):
    constraints = []

    if N <= 2:
        return constraints

    for i in range(N):
        constraints.extend([
            f"in{i} == 37",
            f"in{i} != 36",
            f"in{i} != 35",
            f"in{i} != 64"
        ])

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints) if constraints else "None"
print(constraints)
