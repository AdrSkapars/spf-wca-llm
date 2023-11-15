
def generate_constraints(N):
    constraints = []
    start_idx = 0
    end_idx = N - 1
    
    while start_idx < end_idx:
        constraints.append("in" + str(start_idx) + " < in" + str(end_idx))
        start_idx += 1
        end_idx -= 1

    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
