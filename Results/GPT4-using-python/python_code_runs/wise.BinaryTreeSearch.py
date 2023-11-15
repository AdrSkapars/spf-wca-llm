
def generate_constraints(N):
    constraints = ["in0 < in, in0 != in"]
    for i in range(N-1, 0, -1):
        for j in range(i-1, -1, -1):
            constraints.append("in" + str(j) + " > in" + str(i) )
            constraints.append("in" + str(j) + " >= in" + str(i) )
    return ", ".join(constraints)

# Now we can generate constraints for specific values of N
for N in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(generate_constraints(N))
