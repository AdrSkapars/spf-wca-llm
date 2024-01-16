
def generate_constraints(N):
    constraints = []

    for i in range(N-1, -1, -1):
        constraints.append(f"put{i}_0 != get0")
    
    constraints.append(f"0 == ((get1 + get0) % {N})")

    for i in range(N-1, -1, -1):
        constraints.append(f"0 == ((put{i}_1 + put{i}_0) % {N})")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
