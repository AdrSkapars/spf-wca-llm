
def generate_constraints(N):
    constraints = []
    for i in range(N-1):
        constraints.append(f"in{i} < in{i+1}")
        if i < N-2:
            constraints.append(f"in{i} < in{i+2}")
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
