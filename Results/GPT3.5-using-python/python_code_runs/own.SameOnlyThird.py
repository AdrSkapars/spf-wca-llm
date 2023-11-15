
def generate_constraints(N):
    constraints = []

    if N > 2:
        constraints.append("in2 == 0")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
