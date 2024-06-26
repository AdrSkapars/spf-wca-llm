
def generate_constraints(N):
    constraints = []
    for i in range(2, N):
        constraint = "(in{} - in{}) == (in{} - in{})".format(i, i-1, i-1, i-2)
        constraints.append(constraint)
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
