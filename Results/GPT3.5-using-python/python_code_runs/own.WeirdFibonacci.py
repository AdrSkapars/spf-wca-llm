
def generate_constraints(N):
    constraints = []
    if N < 3:
        return None
    else:
        for k in range(2, N):
            constraints.append(f"in{k} == (in{k-2} + in{k-1})")
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
if constraints:
    constraints = ", ".join(constraints)
else:
    constraints = "None"
print(constraints)
