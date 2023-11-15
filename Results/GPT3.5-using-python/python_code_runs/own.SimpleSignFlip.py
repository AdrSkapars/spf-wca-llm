
def generate_constraints(N):
    constraints = []

    if N == 1:
        return None  # For N=1, no constraints are needed

    for i in range(1, N):  # For each pair of adjacent elements
        constraints.append(f"in{i} == in{i-1}")  # Each element must be equal to its previous element
    
    for i in range(1, N-1):  # For each pair of adjacent elements
        constraints.append(f"in{i} < in{i+1}")  # Each element must be less than the next element
    
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
if constraints:
    constraints = ", ".join(constraints)
else:
    constraints = "None"
print(constraints)
