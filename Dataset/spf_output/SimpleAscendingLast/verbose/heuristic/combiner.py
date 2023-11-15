import ast
import re
from sympy import symbols, Eq, Ne, Lt, Le, Gt, Ge

name = "SimpleAscendingLast"
policies = 30

comb = ""
for count in range(2,policies+1):
	with open("own."+name+"_"+str(count)+".omega", "r") as f:
		read = f.read()[1:-2].replace("&&", ", ").split(":")

	order = "["
	s_string = ""
	for j in range(count):
		dig = str(j)
		if j < 10:
			dig = "0"+dig
		order += "s"+dig+","
		s_string += "s"+dig+" "
	order = order[:-1] + "]"
	# s = symbols(s_string[:-1])

	constraints = read[1]
	for j in range(count, -1, -1):
		dig = str(j)
		if j < 10:
			dig = "0"+dig
		constraints = constraints.replace("ss"+str(j), "s"+dig)
	constraints = constraints[1:]
	relations = {'>': Lt,'>=': Le,'<': Lt,'<=': Le,'==': Eq,'!=': Ne}
	inequalities = []

	# Deal with s00<s01
	pattern = r'(\w+)([<>=!]=?)(\w+)'
	matches = re.findall(pattern, constraints)
	for match in matches:
		op = match[1]
		# s0 = s[int(match[0][-2:])] if match[0][0] == "s" else match[0]
		# s1 = s[int(match[2][-2:])] if match[2][0] == "s" else match[2]
		s0 = symbols(match[0])
		s1 = symbols(match[2])
		if op == '>' or op == '>=':
			op = '<' if op == '>' else '<='
			inequalities.append(relations[op](s1, s0))
		else:
			inequalities.append(relations[op](s0, s1))

	# Deal with (s00-s01)<0
	pattern = r'\((\w+)-(\w+)\)([<>=!]=?)0'
	matches = re.findall(pattern, constraints)
	for match in matches:
		op = match[2]
		s0 = symbols(match[0])
		s1 = symbols(match[1])
		if op == '>' or op == '>=':
			op = '<' if op == '>' else '<='
			# inequalities.append(relations[op](s[int(match[1][-2:])], s[int(match[0][-2:])]))
			inequalities.append(relations[op](s1, s0))
		else:
			# inequalities.append(relations[op](s[int(match[0][-2:])], s[int(match[1][-2:])]))
			inequalities.append(relations[op](s0, s1))

	# # Find transitive inferences
	# inferred_inequalities = set(inequalities)
	# for times in range(policies):
	#	 for i in range(len(inequalities)):
	#		 for j in range(len(inequalities)):
	#			 if i != j:
	#				 if inequalities[i].rhs == inequalities[j].lhs:
	#					 if isinstance(inequalities[i], Lt) and isinstance(inequalities[j], Lt):
	#						 inferred_inequalities.add(Lt(inequalities[i].lhs, inequalities[j].rhs))
	#					 elif isinstance(inequalities[i], Le) and isinstance(inequalities[j], Lt):
	#						 inferred_inequalities.add(Lt(inequalities[i].lhs, inequalities[j].rhs))
	#					 elif isinstance(inequalities[i], Lt) and isinstance(inequalities[j], Le):
	#						 inferred_inequalities.add(Lt(inequalities[i].lhs, inequalities[j].rhs))
	#					 elif isinstance(inequalities[i], Le) and isinstance(inequalities[j], Le):
	#						 inferred_inequalities.add(Le(inequalities[i].lhs, inequalities[j].rhs))
	#					 elif isinstance(inequalities[i], Eq) and isinstance(inequalities[j], Eq):
	#						 inferred_inequalities.add(Eq(inequalities[i].lhs, inequalities[j].rhs))
	#					 elif isinstance(inequalities[i], Ne) and isinstance(inequalities[j], Ne):
	#						 inferred_inequalities.add(Ne(inequalities[i].lhs, inequalities[j].rhs))
	#	 inequalities = list(inferred_inequalities)

	# # Sort inequalities based on their variables
	# inequalities.sort(key=lambda x: (str(x.lhs), str(x.rhs)))
	# inequalities = str(inequalities)[1:-1]

	# comb += "\n\nValid constraints of " + str(count) + " inputs:\n" + order + " such that "+ inequalities



	# Combine two-variable inequalities
	combined_inequalities = []
	for ineq in inequalities:
		 combined_inequalities.append([ineq.lhs, ineq.rel_op, ineq.rhs])

	changed = True
	while changed:
		 changed = False
		 pool_inequalities = []
		 for chain1 in combined_inequalities:
			 here = False
			 for chain2 in combined_inequalities:
				 if chain1[-1] == chain2[0]:
					 changed = True
					 here = True
					 pool_inequalities.append(chain1+chain2[1:])
				 # if chain1[0] == chain2[-1]:
				 #	 print("hey")
				 #	 changed = True
				 #	 pool_inequalities.append(chain2+chain1[1:])
			 if here == False:
				 pool_inequalities.append(chain1)


		 if changed:
			 combined_inequalities = pool_inequalities

	chains = []
	for chain in combined_inequalities:
		 chains.append(" ".join([str(x) for x in chain]))
		 # print(" ".join([str(x) for x in chain]))
	chains.sort(key=lambda x: len(x), reverse=True)

	# Print combined inequalities
	chains2 = []
	for chain in chains:
		 bad = False
		 for chain2 in chains2:
			 if chain in chain2:
				 bad = True
				 break
		 if bad:
			 continue
		 chains2.append(chain)
	
	# string_chains = ",\n".join(chains2)
	string_chains = str(chains2[0])
	comb += "\n\nValid constraints of " + str(count) + " inputs:\n" + order + " such that\n"+ string_chains


	# print(count)

# print(comb)
with open(name+"_chains.txt", "w") as f:
	f.write(comb)