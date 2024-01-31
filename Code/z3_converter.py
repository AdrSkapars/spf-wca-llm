import time

import openai
# openai.api_key = "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" # adrians
openai.api_key = "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" # youchengs
GENERAL_MODEL = "gpt-4"
# GENERAL_MODEL = "gpt-3.5-turbo-1106"
# USING_CODE = True
USING_CODE = False


def get_response(history, prompt, model=GENERAL_MODEL):
	# History is the chat log so far thats submitted to GPT for context
	history.append({"role": "user", "content": prompt})
	done_it = False
	limit = 12
	while not done_it and limit != 0:
		try:
			time.sleep(1)
			response = openai.ChatCompletion.create(
				model=model,
				messages=history,
			)
			done_it = True
			history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
			return response
		except Exception as e:
			print("(gpt error)")
			print(e)
			if str(e).startswith("This model's maximum context length"):
				# Tokens per minute rate has not been exceeded, just message itself is too long to input
				history.pop(-1)
				return -1
			# Most likely tokens per minute rate has been exceeded so wait a little
			limit -= 1
			time.sleep(10)
	return -2

prompts = {
	"get_maths_code": "The following python function takes the parameter N and returns a list of strings. The strings can be interpreted as inequalities or constraints featuring certain variables and constants.\n\n```python\ndef generate_constraints(N):\n    constraints = []\n    for i in range(N):\n        for j in range(i+1, N):\n            constraints.append(f'in{i} != in{j}')\n    return constraints\n```\n\nThis can be converted to a mathematical definition of a set of inequalities. The set definition should be a generalisation for an arbitrary N, the same way that the code can take any input value for N.\n\n```\n{in[i] ≠ in[j] | 0 ≤ i < j < N} for all i, j ∈ Z+ \n```\n\nConvert the following code in the same way, returning your definition in a code block. You may define and join several sets using the union operation if that makes it easier. \n\n",
	"get_maths_llm": "The following set description defines a generalisation over a set of inequalities or constraints featuring certain variables and constants. It is parametrised by N, which is the amount of unique variables that the constraints may contain. \n\n```\nTaking into account that the constraints should be ordered in a descending order as per the variables used and the input values (i.e., greatest to smallest), a generalisation of these constraints for N inputs would be formatted as:\n\nFor i from N-2 down to 0:\n    For j from N-1 down to i+1:\n        Add the constraint 'in[i] != in[j]'\n\nThis adds a sequence of constraints starting from 'inN-2', and each 'in[i]' is compared for inequality with the next higher inputs ('in[i+1]', 'in[i+2]', ..., 'in[N-1]'). \n```\n\nThis can be converted to a mathematical definition of a set of inequalities. The set definition should be a generalisation for an arbitrary N.\n\n```\n{{in[i] ≠ in[j] | 0 ≤ i < j < N} for all i, j ∈ Z+  \n```\n\nConvert the following description in the same way, returning your definition in a code block. You may define and join several sets using the union operation if that makes it easier.\n\n",
	"get_z3_from_maths": "Here is the previous example of a The example mathematical definition of a set of inequalities.\n\n```\n{in[i] ≠ in[j] | 0 ≤ i < j < N} for all i, j ∈ Z+ \n```\n\nThis can be further converted to the syntax of the z3 solver in Python.\n\n```python\nN = Int('N')\nss = Function('ss', IntSort(), IntSort())\ni = Int('i')\nj = Int('j')\n\n# for all i, for all j, ((0 ≤ i < j < N) -> ss[i] != ss[j])\nprediction = ForAll([i, j], Implies(And(0 <= i, i < j, j < N), ss(i) != ss(j)))\n```\n\nHere is your mathematical definition again.\n```\n{in[i-1] = in[i]  |  1 ≤ i < (N+2)//2} ∪ {in[i-1] < in[i]  |  (N+2)//2 ≤ i < N} for all i ∈ Z+\n```\n\nConvert this to the syntax of the z3 solver in Python, the same way as the example. Start your code with the lines \"N = Int('N')\" and \"ss = Function('ss', IntSort(), IntSort())\" and have the final specification be stored in the 'prediction' variable. Notice how the Function/array of variables is always called 'ss' when converted, even though its called 'in' in the original maths. If you need to use a two dimensional function, define it as 'ss = Function('ss', IntSort(), IntSort(), IntSort())'. Also make sure to write it in parenthesis (e.g. ss(i)) instead of square brackets (e.g. ss[i]). Also make sure to split 0 <= i < N to And(0 <= i, i < N). Also make sure to use '/' division instead of '//' since they are equivalent.\n\n",
}


gen_files = [
	"generals/own.SameHundred",
	"generals/own.SameLowercase",
	"generals/own.SameOnlyThird",
	"generals/own.SameString",
	"generals/own.SimpleAscendingLast",
	"generals/own.SimpleEveryThird",
	"generals/own.SimpleSignFlip",
	"generals/own.SimpleSymmetric",
	"generals/own.SimpleTrueFalse",
	"generals/own.SimpleUnique",
	"generals/own.WeirdConstDiff",
	"generals/own.WeirdFibonacci",
	"generals/own.WeirdTimes",
	"generals/own.BadgerHash",
	"generals/own.BadgerPassword",
	"generals/own.BadgerUsername",
	"generals/own.ComplexFlipPos_1",
	"generals/own.ComplexFlipPos_2",
	"generals/own.ComplexHalfEqual",
	"generals/own.ComplexMidPeak",
	"generals/own.ComplexPalindrome",
	"generals/own.ComplexOddsEvens",
]

for file_path in gen_files:
	history = []
	# Get maths format from generalisation format
	# Prepare the prompt
	get_maths = "get_maths_code" if USING_CODE else "get_maths_llm"
	get_maths = prompts[get_maths]
	block = "```python" if USING_CODE else "```"
	file_end = ".py" if USING_CODE else ".txt"
	with open(file_path+file_end, "r") as f:
		gen = f.read()
	if USING_CODE:
		gen = gen.split("N = int(input(\"N=\"))")[0]
		while gen[-1] in ["\n", " "]:
			gen = gen[:-1]
	get_maths = get_maths + block + "\n" + gen + "\n```"
	print("\n"+"#"*60)
	print(get_maths)

	# Get response given to the prompt
	response_get_maths = get_response(history, get_maths)
	content_get_maths = response_get_maths['choices'][0]['message']['content']
	print("\n"+"#"*60)
	print(content_get_maths)

	# Make sure response is correctly formatted
	gen_limit = 5
	while len(content_get_maths.split("```")) != 3 and gen_limit != 0:
		# Response isnt returning single code block
		maths_message = "Please write the final definition in a single code block. Do not have any other code blocks in your response."
		print("\n"+"#"*60)
		print(maths_message)

		response_get_maths = get_response(history, maths_message)
		content_get_maths = response_get_maths['choices'][0]['message']['content']
		print("\n"+"#"*60)
		print(content_get_maths)
		gen_limit -= 1

	maths_format = content_get_maths.split("```")[1]

	# Now convert that to z3 format
	# Prepare the prompt
	get_z3 = prompts["get_z3_from_maths"]
	get_z3 = get_z3 + "```\n" + maths_format + "\n```"
	print("\n"+"#"*60)
	print(get_z3)

	# Get response given to the prompt
	response_get_z3 = get_response(history, get_z3)
	content_get_z3 = response_get_z3['choices'][0]['message']['content']
	print("\n"+"#"*60)
	print(content_get_z3)

	# Make sure response is correctly formatted
	gen_limit = 5
	while len(content_get_z3.split("```")) != 3 and gen_limit != 0:
		# Response isnt returning single code block
		z3_message = "Please write the final z3 definition in a single code block. Do not have any other code blocks in your response."
		print("\n"+"#"*60)
		print(z3_message)

		response_get_z3 = get_response(history, z3_message)
		content_get_z3 = response_get_z3['choices'][0]['message']['content']
		print("\n"+"#"*60)
		print(content_get_z3)
		gen_limit -= 1

	z3_format = content_get_z3.split("```")[1].replace("python\n", "")

	# Save z3 solution in file
	z3_name = file_path.split("/")[-1]
	z3_path = "z3_generals/"+str(z3_name)+".py"
	with open(z3_path, "w") as f:
		f.write(z3_format)
