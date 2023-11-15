
def generate_constraints(N):
    constraints = []
    for i in range(N):
        constraints.append(f"in{i} == 45")
        constraints.append(f"in{i} != 95")
    
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
print(constraints)
