
def generate_constraints(N):
    constraints = []

    for i in range(2, N):  
        constraint = f"in{i} == (in{i-2} + in{i-1})"
        constraints.append(constraint)

    return ", ".join(constraints)

N = int(input("N="))
constraints = generate_constraints(N)
print(constraints)
