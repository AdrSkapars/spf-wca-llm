
def generate_constraints(N):
    constraints = []
    if N > 2:
        for i in range(N):
            constraints.append(f"in{i} == 45")
            constraints.append(f"in{i} != 95")
    return constraints if N > 2 else []

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
