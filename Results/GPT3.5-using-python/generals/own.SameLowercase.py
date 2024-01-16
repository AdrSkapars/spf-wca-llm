
def generate_constraints(N):
    constraints = []

    for i in range(N-1, -1, -1):
        constraints.append(f"in{i} <= 122")
        constraints.append(f"in{i} >= 97")
        if i > 0:
            for j in range(i-1, -1, -1):
                constraints.append(f"in{j} <= 122")
                constraints.append(f"in{j} >= 97")

    # Remove duplicate inequalities
    constraints = list(set(constraints))

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
