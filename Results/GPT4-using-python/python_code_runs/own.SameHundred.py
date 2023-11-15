
def generate_constraints(N):
    constraints = []
    for i in range(1, N):
        constraints.append("in{} >= 100".format(i))
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
