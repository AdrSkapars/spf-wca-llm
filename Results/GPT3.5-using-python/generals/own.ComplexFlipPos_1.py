
def generate_constraints(N):
    constraints = []
    for i in range(N):
        for j in range(i):
            constraints.append("in{} < in{}".format(j, i))
    return constraints
