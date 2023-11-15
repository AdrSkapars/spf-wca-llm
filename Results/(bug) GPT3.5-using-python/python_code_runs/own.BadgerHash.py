
def generate_output_constraint_set(N):
    constraints = []
    constraints.append(f"put0_0 != get0")
    constraints.append(f"0 == ((get1 + get0) % {N})")
    for i in range(N):
        constraints.append(f"put{i}_0 != get0")
        constraints.append(f"0 == ((put{i}_1 + put{i}_0) % {N})")
    
    return constraints
