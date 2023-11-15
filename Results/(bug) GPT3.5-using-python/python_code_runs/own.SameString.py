
def generate_constraints(N):
    constraints = []

    for i in range(N-1, -1, -1):
        constraints.append(f"in{i} == 120")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
