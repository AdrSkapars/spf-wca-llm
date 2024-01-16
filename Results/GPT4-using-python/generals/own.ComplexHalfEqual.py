
def generate_constraints(N):
    constraints = []
    for i in range(1, N):
        if i < (N+2)//2:
            constraints.append(f"in{i-1} == in{i}")
        else:
            constraints.append(f"in{i-1} < in{i}")
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
