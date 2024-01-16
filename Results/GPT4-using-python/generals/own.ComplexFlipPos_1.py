
def generate_constraints(N):
    constraints = []
    
    for i in range(0, N, 4):
        # Base constraints for each group of four
        if i + 3 < N:
            constraints.append(f"in{i+3} < in{i+2}")
            constraints.append(f"in{i+1} < in{i}")
            constraints.append(f"in{i} < in{i+3}")
        elif i + 2 < N:
            constraints.append(f"in{i+2} < in{i+1}")
            constraints.append(f"in{i+1} < in{i+2}")
        elif i + 1 < N:
            constraints.append(f"in{i+1} < in{i}")
        
        # Extra constraints for sets starting with a number 1 more than a multiple of 2
        if i != 0 and i % 4 == 1:
            if i + 3 < N:
                constraints.append(f"in{i+2} < in{i+1}")
                constraints.append(f"in{i+1} < in{i+3}")
        
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
