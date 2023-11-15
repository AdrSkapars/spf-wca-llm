
def generate_constraints(N):
    constraints = []
    for i in range(N, 3, -1):
        if i % 3 == 0:
            constraints.append(f"in{i} == 0")
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
