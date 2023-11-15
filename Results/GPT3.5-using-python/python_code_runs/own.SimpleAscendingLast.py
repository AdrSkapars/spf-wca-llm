
def generate_constraints(N):
    constraints = []
    for i in range(1, N):
        constraints.append(f"in{i} < in0")  # Each variable at a higher index is less than in0
        constraints.append(f"in0 < in{i}")  # in0 is less than each variable at a higher index
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
