
def generate_constraints(N):
    constraints = ["in" + str(i) + " == " + str((i + 1) % 2) for i in range(N-1, -1, -1)]
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
