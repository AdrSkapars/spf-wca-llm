
def generate_constraints(N):
    constraints = []

    for i in range(N):
        constraints.append(f"in{i} >= 100")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
