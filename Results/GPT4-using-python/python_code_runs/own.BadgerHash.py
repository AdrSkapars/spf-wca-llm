
def generate_constraints(N):
    constraints = []

    for i in range(N-1, -1, -1):
        constraints.append("put{}_0 != get0".format(N-i-1))

    for i in range(N-1, -1, -1):
        constraints.append("0 == ((put{}_1 + put{}_0) % {})".format(N-i-1, N-i-1, N))

    constraints.append("0 == ((get1 + get0) % {})".format(N))

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
