
def generate_constraints(N):
    constraints = []
    for i in range(3, N + 1, 3):  # Start from 3 and increment in steps of 3
        if N > i:  # Only add constraint if total input number is greater
            constraints.insert(0, f'in{i} == 0')  # Insert constraint at the beginning of the list
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
