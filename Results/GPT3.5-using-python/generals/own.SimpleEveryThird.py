
def generate_constraints(N):
    constraints = []
    for i in range(2, N):
        if N % i == 0:
            constraints.append(f"in{N-i+1} == 0")
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
