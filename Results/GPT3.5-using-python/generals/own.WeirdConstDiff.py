
def generate_constraints(N):
    constraints = []

    for i in range(2, N):
        constraints.append(f"(in{i} - in{i-1}) == (in{i-1} - in{i-2})")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
