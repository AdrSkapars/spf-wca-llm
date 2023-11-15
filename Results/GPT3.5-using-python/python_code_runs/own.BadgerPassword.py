
def generate_constraints(N):
    if N < 1:
        return None
    elif N == 1:
        return None
    else:
        constraints = []
        for i in range(N):
            individual_constraint = f"in{i} == 37, in{i} != 36, in{i} != 35, in{i} != 64"
            constraints.append(individual_constraint)

            if i > 0:
                pairwise_constraint = f"in{i} == 37, in{i} != 36, in{i} != 35, in{i} != 64, in{i-1} == 37, in{i-1} != 36, in{i-1} != 35, in{i-1} != 64"
                constraints.append(pairwise_constraint)
                
        return ", ".join(constraints)

N = int(input("N="))
constraints = generate_constraints(N)
print(constraints)
