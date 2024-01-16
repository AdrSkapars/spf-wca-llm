
def generate_constraints(N):
    constraints = []

    if N > 1:
        constraints.append(f"in{N-1} < in0")

    if N > 2:
        for i in range(1, N-1, 2):
            constraints.append(f"in{i} < in0")
        for j in range(0, N-1, 2):
            constraints.append(f"in{j} < in{j+2}")

    return constraints[::-1] # Reverse to match desired order

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
