
def generate_constraints(N):
    constraints = []
    for i in range(N):
        for j in range(i+1, N):
            constraints.append("in{}x{} == in{}x{}".format(j, i, i, j))
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
