
def generate_constraints(N):
    constraints = [f"in{N-i-1} < in{N-i}" for i in range(N-1)]
    return ", ".join(constraints)

N = int(input("N="))
constraints = generate_constraints(N)
print(constraints)
