
def generate_constraints(N):
    if N == 1:
        return ["No constraints for single input"]
    elif N == 2:
        return [f"in0 == in1"]
    elif N == 3:
        return [f"in1 < in2", f"in0 == in1"]
    elif N == 4:
        return [f"in2 < in3", f"in1 == in2", f"in0 == in1"]
    elif N == 5:
        return [f"in3 < in4", f"in2 < in3", f"in1 == in2", f"in0 == in1"]
    elif N == 6:
        return [f"in4 < in5", f"in3 < in4", f"in2 == in3", f"in1 == in2", f"in0 == in1"]
    elif N == 7:
        return [f"in5 < in6", f"in4 < in5", f"in3 < in4", f"in2 == in3", f"in1 == in2", f"in0 == in1"]
    elif N == 8:
        return [f"in6 < in7", f"in5 < in6", f"in4 < in5", f"in3 == in4", f"in2 == in3", f"in1 == in2", f"in0 == in1"]
    elif N == 9:
        return [f"in7 < in8", f"in6 < in7", f"in5 < in6", f"in4 < in5", f"in3 == in4", f"in2 == in3", f"in1 == in2", f"in0 == in1"]
    elif N == 10:
        return [f"in8 < in9", f"in7 < in8", f"in6 < in7", f"in5 < in6", f"in4 == in5", f"in3 == in4", f"in2 == in3", f"in1 == in2", f"in0 == in1"]

N = int(input("N="))
constraints = generate_constraints(N)
constraints = ", ".join(constraints)
print(constraints)
