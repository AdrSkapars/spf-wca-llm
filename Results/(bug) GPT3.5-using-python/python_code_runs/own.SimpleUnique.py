
def generate_constraints(N):
    constraints = []
    for i in range(N-1):
        for j in range(i+1, N):
            constraints.append(f"in{i} != in{j}")
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
