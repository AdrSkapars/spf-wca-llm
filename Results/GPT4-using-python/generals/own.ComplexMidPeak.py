
def generate_constraints(N):
    constraints = []

    for i in range(N-1):
        if i < N//2:
            constraints.append('in{} < in{}'.format(i, i+1))
        else:
            constraints.append('in{} > in{}'.format(i, i+1))
    
    return constraints

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
