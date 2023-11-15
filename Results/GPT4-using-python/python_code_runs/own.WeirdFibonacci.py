
def generate_constraints(N):
    constraints = []
    if N > 2:
        for i in range(N-1, 1, -1):
            constraints.append("in{} == (in{} + in{})".format(i, i-2, i-1))
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
