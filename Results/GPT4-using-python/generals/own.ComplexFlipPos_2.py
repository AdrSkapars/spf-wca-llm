
def generate_constraints(N):
    constraints = []

    # 'in_(i) < in_(i-1)' constraints
    for i in range(N-1, 0, -2):
        constraints.append(f"in{i} < in{i-1}")

    # 'in_0 < in_(N-1)' constraints
    for i in range(N-1, 2, -2):
        constraints.append(f"in0 < in{i}")
        
    # 'in1 < in0' constraint
    if N > 1:
        constraints.append(f"in1 < in0")
        
    # 'in_(N-4) < in_(N-2)' constraints
    for i in range(4, N, 2):
        constraints.append(f"in{i-2} < in{i}")
        
    return constraints

N = int(input("N = "))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
