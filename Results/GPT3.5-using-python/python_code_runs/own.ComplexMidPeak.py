
def generate_constraints(N):
    constraints = []

    for i in range(N-1):
        if i % 2 == 0:
            constraints.append(f'in{i+1} > in{i}')
        else:
            constraints.append(f'in{i} < in{i+1}')

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
