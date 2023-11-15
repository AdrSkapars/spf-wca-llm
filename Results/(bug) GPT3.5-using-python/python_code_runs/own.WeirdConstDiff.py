
def generate_constraints(N):
    constraints = []
    if N >= 3:
        for i in range(2, N):
            constraint = f"(in{i} - in{i-1}) == (in{i-1} - in{i-2})"
            constraints.append(constraint)
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
