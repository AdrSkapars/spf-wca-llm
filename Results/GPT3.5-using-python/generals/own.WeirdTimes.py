
def generate_constraints(N):
    constraints = []
    for k in range(1, N):
        constraints.append(f"in{N-k} == (in0 * {N-k+1})")
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
