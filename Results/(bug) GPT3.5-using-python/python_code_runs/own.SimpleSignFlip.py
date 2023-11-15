
def generate_constraints(N):
    constraints = []

    for i in range(N-1):
        constraints.append(f"in{i} <= in{i+1}")

    for j in range(N-1):
        constraints.append(f"in{j} == in{j+1}")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
