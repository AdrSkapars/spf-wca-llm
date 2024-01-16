
def generate_constraints(N):
    constraints = []

    if N>=3:
        for i in range(N):
            constraints.append('in' + str(i) + ' == 45')
            constraints.append('in' + str(i) + ' != 95')

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
