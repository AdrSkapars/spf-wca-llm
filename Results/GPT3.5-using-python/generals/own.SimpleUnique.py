
def generate_constraints(N):
    constraints = []

    for i in range(N):
        for j in range(i):
            constraints.append(f'in{j} != in{i}')

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
