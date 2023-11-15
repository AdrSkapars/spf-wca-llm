
def generate_constraints(N):
    constraints = []

    for i in range(N):
        constraints.append(f"in{i+1} == (in0 * {N-i-1})")

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
if constraints:
    constraints = ", ".join(constraints)
else:
    constraints = "None"
print(constraints)
