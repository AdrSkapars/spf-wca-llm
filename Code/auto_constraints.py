import csv
import json
import time

import subprocess

import openai
# openai.api_key = "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" # adrians
openai.api_key = "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" # youchengs
# GENERAL_MODEL = "gpt-4"
GENERAL_MODEL = "gpt-3.5-turbo-1106"

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

def print_and_save(conversation, new_message):
	print("\n"+"#"*60)
	print(new_message)
	conversation.append("\n"+"#"*60+"\n")
	conversation.append(new_message)
	# stop = input("(ENTER to continue)")


prompts = {
	"get_gen_sys_code": "Always respond first with an informal analysis in natural language and maybe some mathematics (under the heading 'CASUAL', all caps), then with a formal Python program answer inside a code block (under the heading 'FORMAL', all caps). Make sure there is only one code block in your answer.",
	"get_gen_sys_llm": "Always respond first with an informal analysis in natural language (under the heading 'CASUAL', all caps), then with a formal/ mathematical answer (under the heading 'FORMAL', all caps). Make no further comments after the formal section like 'This should hold true', for example.",
	"get_gen_start": "I'm experimenting with a program and trying to find what makes an increasingly large set of inputs valid. So far I have found one possible set of correct constraints/ conditions (not the only one) which define a valid input. Here they are.",
	"get_gen_end": "\n\nGeneralise what makes the set of constraints valid such that we can recover a valid set for N inputs. Don't overfit the data here but also dont oversimplify to the point of trivialness. Make sure none of the given examples contradict your generalisation.",
	"get_gen_end_code1": "\n\nUse this code template to formally express the generalisation for N constraints:\n```python\n",
	"get_gen_end_code2": "```\n\nEach inequality is usually in the form \"x op y\" where x, y are some variable, constant or some formula of variables and/ or constants, and op is an operation or inequality.",
	"apply_gen_sys": "Always respond first with a step by step application of the generalisation (under the heading 'WORKING OUT', all caps), then with the final answer (under the heading 'ANSWER', all caps), giving the answer as a comma seperated list of constraints without any other natural language like 'here is the set'. If the answer is the empty set just put 'None' as the answer. Make no further comments after the answer section, like 'This is what the generalisation says should hold' for example, just stop.",
	"apply_gen_start": "I have a generalisation definining a set of inequalities for a set of variables. The definition is general for an arbitrary N amount of variables. Here is the generalisation:\n\n```\n",
	"compare_sys": "Always respond first with your thinking process (under the heading 'THINKING', all caps), then with the final answer of 'MATCHES'(all caps) if matches or 'DIFFERENT'(all caps) if doesnt match (under the heading 'ANSWER', all caps), then reiterate the place/ reason it does not match  (under the heading 'REASON', all caps).", 
	"compare_start": "I have two sets of inequalities over variables. Tell me if these two sets are the same or not, and how they differ if they do. Ignore the order of constraints and differences in formatting (e.g spaces, newline characters and exact variable names ('s_0', 's0', 's(0)', '\{s_0\}' and so on are all the same), also ignore any text that isnt a constraints like 'here is the set:') though the numbers associated with variable names should be the same. 'There are no constraints' or 'None' or anything like that is equivalent to '' or the empty set/ string. If the only difference between the two is formatting then they actually match. They're only different if one set is bigger than the other or if they contain constraints that aren't in the other. Try to keep your final reasons short but not generic and without using bullet points or numbered lists.\n\n",
	"new_gen_start_code": "I have run your code for several concrete values of N. Some of the outputs were not correct. Change your generalisation and code to account for the following outputs (Remember to always structure your reply with the headings 'CASUAL' and 'FORMAL').\n\n",
	"new_gen_start_llm": "Remember to always structure your reply with the same headings. I have applied you generalisation for several concrete values of N. Some of the outputs were not correct. Change your generalisation to account for the following outputs (Remember to always structure your reply with the headings 'CASUAL' and 'FORMAL').\n\n",
}
	# "/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SameHundred/verbose/heuristic/own.SameHundred.csv",
	# "/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SameLowercase/verbose/heuristic/own.SameLowercase.csv",
	
csv_files = [
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SameOnlyThird/verbose/heuristic/own.SameOnlyThird.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SameString/verbose/heuristic/own.SameString.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SimpleAscendingLast/verbose/heuristic/own.SimpleAscendingLast.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SimpleEveryThird/verbose/heuristic/own.SimpleEveryThird.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SimpleSignFlip/verbose/heuristic/own.SimpleSignFlip.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SimpleSymmetric/verbose/heuristic/own.SimpleSymmetric.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SimpleTrueFalse/verbose/heuristic/own.SimpleTrueFalse.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/SimpleUnique/verbose/heuristic/own.SimpleUnique.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/WeirdConstDiff/verbose/heuristic/own.WeirdConstDiff.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/WeirdFibonacci/verbose/heuristic/own.WeirdFibonacci.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/WeirdTimes/verbose/heuristic/own.WeirdTimes.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/BadgerHash/verbose/heuristic/own.BadgerHash.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/BadgerPassword/verbose/heuristic/own.BadgerPassword.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/BadgerUsername/verbose/heuristic/own.BadgerUsername.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/ComplexFlipPos_2/verbose/heuristic/own.ComplexFlipPos.csv",#
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/ComplexHalfEqual/verbose/heuristic/own.ComplexHalfEqual.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/ComplexMidPeak/verbose/heuristic/own.ComplexMidPeak.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/ComplexPalindrome/verbose/heuristic/own.ComplexPalindrome.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/ComplexOddsEvens/verbose/heuristic/own.ComplexOddsEvens.csv",
	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/ComplexFlipPos_1/verbose/heuristic/own.ComplexFlipPos.csv",
]

# Constraints too long
#	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results_own/WeirdLoopMean/verbose/heuristic/own.WeirdLoopMean.csv",
#	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results/dijkstra_results/verbose/heuristic/wise.Dijkstra.csv",
#	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results/binary_tree_search_results/verbose/heuristic/wise.BinaryTreeSearch.csv",
#	"/home/adrians/Documents/Masters/Java_PathFinder/spf-wca/results/tsp_results/verbose/heuristic/wise.Tsp.csv",


USING_CODE = False
# USING_CODE = True
MAX_EXAMPLES = 10
MAX_ATTEMPTS = 10
experiment_stats = {}

for file_path in csv_files:
	gen_sys = "get_gen_sys_code" if USING_CODE else "get_gen_sys_llm"
	llm_get_gen = [{"role": "system", "content": prompts[gen_sys]}]
	
	conversation = []
	convo_stats = {}
	# Get constraints from SPF
	constraints = []
	with open(file_path, 'r') as file:
		reader = csv.reader(file)
		next(reader) # Skip the header row
		for example_id in range(MAX_EXAMPLES):
			row = next(reader)
			con = row[12]
			# Preprocess format of constraints
			con = con.replace("CONST_", "").replace(" &&", ",").replace("CONSTRAINT N/A", "None")
			constraints.append(con)

	# Get inital generalisation
	print_and_save(conversation, " "*20+"GET INITIAL GENERALISATION")
	prompt_get_gen = prompts["get_gen_start"]
	for example_id in range(MAX_EXAMPLES):
		prompt_get_gen += f"\n\nValid constraints for {example_id+1} inputs (N={example_id+1}):\n"
		prompt_get_gen += str(constraints[example_id])
	prompt_get_gen += prompts["get_gen_end"]
	if USING_CODE:
		prompt_get_gen += prompts["get_gen_end_code1"]
		with open("python_code_runs/python_code_template.py", "r") as file:
			prompt_get_gen += file.read()
		prompt_get_gen += prompts["get_gen_end_code2"]
	print_and_save(conversation, prompt_get_gen)

	response_get_gen = get_response(llm_get_gen, prompt_get_gen)
	content_get_gen = response_get_gen['choices'][0]['message']['content']
	print_and_save(conversation, content_get_gen)

	generalisation_empty = "FORMAL" in content_get_gen and len(content_get_gen.split("FORMAL")[1]) < 10
	gen_limit = 5
	while ("FORMAL" not in content_get_gen or generalisation_empty) and gen_limit != 0:
		# Response not using correct headings, repeat formatting instructions to LLM
		gen_message = prompts[gen_sys]
		if generalisation_empty:
			# gen_message = "You don't have anything under the 'FORMAL' heading. " + gen_message
			gen_message = "Your response stopped short. Continue where you left off with a new line character and the heading 'FORMAL'."				

		print_and_save(conversation, gen_message)
		response_get_gen = get_response(llm_get_gen, gen_message)
		content_get_gen = response_get_gen['choices'][0]['message']['content']
		print_and_save(conversation, content_get_gen)
		generalisation_empty = "FORMAL" in content_get_gen and len(content_get_gen.split("FORMAL")[1]) < 10
		gen_limit -= 1

	generalisation = content_get_gen.split("FORMAL")[1]

	while generalisation[0] in [":", "\n", " "]:
		generalisation = generalisation[1:]
	while generalisation[-1] in ["\n", " "]:
		generalisation = generalisation[:-1]
	if USING_CODE:
		generalisation = generalisation.split("```")[1].replace("python", "")
		# Sometimes the returned code leaves out the print part of template
		if "return" in generalisation.split("\n")[-1]:
			generalisation += "\n\nN = int(input(\"N=\"))\nconstraints = generate_constraints(N)\nconstraints = \", \".join(constraints)\nprint(constraints)"

	# Evaluate prediction
	for attempt_id in range(MAX_ATTEMPTS):
		print_and_save(conversation, " "*20+f"ATTEMPT NUMBER {attempt_id+1}")
		# Use available N examples to evaluate
		eval_results = []
		if USING_CODE:
			test_name = file_path.split("/")[-1][:-4]
			test_path = "python_code_runs/"+str(test_name)+".py"
			with open(test_path, "w") as file:
				file.write(generalisation)

		for example_id in range(MAX_EXAMPLES):
			# print_and_save(conversation, " "*20+f"#{attempt_id+1}  EVALUATING EXAMPLE NUMBER {example_id+1}")
			print(" "*20+f"#{attempt_id+1}  EVALUATING EXAMPLE NUMBER {example_id+1}")
			example_eval = {}
			# Apply generalisation to current N
			if USING_CODE:
				# Do this by using a python interpreter
				try:
					input_data = str(example_id+1)
					output = subprocess.run(["python3", test_path], input=input_data, text=True, capture_output=True, check=True)
					prediction = output.stdout[2:]
					example_eval["prediction"] = prediction
					encountered_error = False
				except subprocess.CalledProcessError as e:
					# If python error has occured, save it so can give it as feedback
					prediction = e.stderr[2:]
					example_eval["prediction"] = prediction
					encountered_error = True
				code_record = "Input: "+str(input_data)+",\nOutput: "+example_eval["prediction"]
				# print_and_save(conversation, code_record)

			else:
				# Do this by using an LLM
				llm_apply_gen = [{"role": "system", "content": prompts["apply_gen_sys"]}]
				prompt_apply_gen = prompts["apply_gen_start"]
				prompt_apply_gen += generalisation + "\n```\n\n"
				prompt_apply_gen +=  f"Apply this generalisation for N={example_id+1} to get the set of inequalities."
				# print_and_save(conversation, prompt_apply_gen)

				response_apply_gen = get_response(llm_apply_gen, prompt_apply_gen)
				content_apply_gen = response_apply_gen['choices'][0]['message']['content']
				# print_and_save(conversation, content_apply_gen)

				answer_limit = 10
				answer_index_error = "ANSWER" in content_apply_gen and len(content_apply_gen.split("ANSWER")[1].replace("\n", "").replace(":", "").replace(" ", "")) == 0
				while (("ANSWER" not in content_apply_gen) or answer_index_error) and answer_limit != 0:
					# Response not using correct headings, repeat formatting instructions to LLM
					# print_and_save(conversation, prompts["apply_gen_sys"])
					print("(bad answer)")
					# response_apply_gen = get_response(llm_apply_gen, "Please provide the comma seperated answer under the heading 'ANSWER'")
					response_apply_gen = get_response(llm_apply_gen, prompts["apply_gen_sys"])
					content_apply_gen = response_apply_gen['choices'][0]['message']['content']
					# print_and_save(conversation, content_apply_gen)
					answer_limit -= 1
				prediction = content_apply_gen.split("ANSWER")[1]
				while len(prediction) != 0 and prediction[0] in ["\n", ":", " "]:
					prediction = prediction[1:]
				example_eval["prediction"] = prediction

			# Compare prediction against ground truth
			# First check if error occured
			if USING_CODE and encountered_error:
				example_eval["matches"] = False
				example_eval["reason"] = "ERROR"
				eval_results.append(example_eval)
				continue

			# Manually check if matches
			compare1 = constraints[example_id].replace(" ", "").replace("\n", "")
			compare2 = prediction.replace(" ", "").replace("\n", "")
			# # Check whether prediction is actually none and whether should be
			# if compare2 == "" or compare2 == "None":
			# 	if compare1 == "None":
			# 		example_eval["matches"] = True
			# 		eval_results.append(example_eval)
			# 		# print("(manually confirmed that matches)")
			# 		continue
			# 	else:
			# 		example_eval["matches"] = False
			# 		example_eval["reason"] = "Predicted no constraints but the correct set is not empty"
			# 		eval_results.append(example_eval)
			# 		# print("(manually confirmed that DOESNT match)")
			# 		continue
			# else:
			# 	if compare1 == "None":
			# 		example_eval["matches"] = False
			# 		example_eval["reason"] = "The correct set is empty but your constraint set is not empty"
			# 		eval_results.append(example_eval)
			# 		# print("(manually confirmed that DOESNT match)")
			# 		continue

			# Check whether the sets are the same while ignoring order or spaces
			if len(compare1) == len(compare2):
				compare1 = compare1.split(",")
				compare2 = compare2.split(",")
				missing = len(compare1)
				for condition in compare1:
					if condition in compare2:
						missing -= 1
				if missing == 0:
					example_eval["matches"] = True
					eval_results.append(example_eval)
					# print("(manually confirmed that matches)")
					continue

			# If can't tell manually if matches, use LLM
			llm_compare = [{"role": "system", "content": prompts["compare_sys"]}]
			prompt_compare = prompts["compare_start"]
			prompt_compare += "Here is the correct set:\n"
			prompt_compare += "```\n" + constraints[example_id] + "\n```\n\n"
			prompt_compare += "Here is the predicted set:\n"
			prompt_compare += "```\n" + prediction + "\n```"
			print_and_save(conversation, prompt_compare[len(prompts["compare_start"]):])

			response_compare = get_response(llm_compare, prompt_compare, model="gpt-3.5-turbo-1106")
			content_compare = response_compare['choices'][0]['message']['content']
			# print_and_save(conversation, content_compare)

			is_match = "MATCHES" in content_compare
			is_different = "DIFFERENT" in content_compare
			is_reason = "REASON" in content_compare
			reason_limit = 5
			while ((not is_match and not is_different) or (is_different and not is_reason)) and reason_limit != 0:
				# Response not using correct headings, repeat formatting instructions to LLM
				# print_and_save(conversation, prompts["compare_sys"])
				response_compare = get_response(llm_compare, prompts["compare_sys"])
				content_compare = response_compare['choices'][0]['message']['content']
				# print_and_save(conversation, content_compare)
				is_match = "MATCHES" in content_compare
				is_different = "DIFFERENT" in content_compare
				is_reason = "REASON" in content_compare
				reason_limit -= 1

			if "MATCHES" in content_compare:
				example_eval["matches"] = True
				eval_results.append(example_eval)
				continue

			example_eval["matches"] = False

			reason = content_compare.split("REASON")[1]
			while reason[0] in ["\n", ":", " "]:
				reason = reason[1:]
			example_eval["reason"] = reason

			eval_results.append(example_eval)

		# Break if all predictions were correct
		true_matches = [example_eval["matches"] for example_eval in eval_results]
		if False not in true_matches:
			convo_stats["succeeded"] = True
			convo_stats["attempts"] = attempt_id+1
			convo_stats["examples_right"] = MAX_EXAMPLES
			break

		# Break if this was the last attempt at generalising
		if attempt_id+1 == MAX_ATTEMPTS:
			convo_stats["succeeded"] = False
			convo_stats["attempts"] = MAX_ATTEMPTS
			convo_stats["examples_right"] = true_matches.count(True)
			break

		# Otherwise give back all the feedback and get new generalisation
		print_and_save(conversation, " "*20+f"#{attempt_id+1}  GET NEW GENERALISATION")
		prompt_get_gen = prompts["new_gen_start_code"] if USING_CODE else prompts["new_gen_start_llm"]
		for example_id in range(MAX_EXAMPLES):
			if eval_results[example_id]["matches"]:
				prompt_get_gen += f"For N={example_id+1}, the generalisation output correctly fits the given data\n\n"
			elif eval_results[example_id]["reason"] == "ERROR":
				prompt_get_gen += f"For N={example_id+1}, there was an error in the code:\n"
				prompt_get_gen += eval_results[example_id]["prediction"] + "\n\n"
			else:
				prompt_get_gen += f"For N={example_id+1}, the output constraint set should be:\n"
				prompt_get_gen += "```\n" + constraints[example_id] + "\n```\n"
				prompt_get_gen += "But your generalisation implies the set:\n"
				prompt_get_gen += "```\n" + eval_results[example_id]["prediction"] + "\n```\n"
				prompt_get_gen += "This is not right. Explanation: " + eval_results[example_id]["reason"] + "\n\n"
		prompt_get_gen = prompt_get_gen[:-2]
		print_and_save(conversation, prompt_get_gen)

		response_get_gen = get_response(llm_get_gen, prompt_get_gen)
		while response_get_gen == -1:
			print("(truncating conversation)")
			llm_get_gen.pop(1)
			llm_get_gen.pop(1)
			llm_get_gen.pop(1)
			llm_get_gen.pop(1)
			time.sleep(30)
			response_get_gen = get_response(llm_get_gen, prompt_get_gen)
		content_get_gen = response_get_gen['choices'][0]['message']['content']
		print_and_save(conversation, content_get_gen)

		generalisation_empty = "FORMAL" in content_get_gen and len(content_get_gen.split("FORMAL")[1]) < 10
		gen_limit = 5
		while ("FORMAL" not in content_get_gen or generalisation_empty) and gen_limit != 0:
			# Response not using correct headings, repeat formatting instructions to LLM
			gen_message = prompts[gen_sys]
			if generalisation_empty:
				# gen_message = "You don't have anything under the 'FORMAL' heading. " + gen_message
				gen_message = "Your response stopped short. Continue where you left off with the heading 'FORMAL'."				
			print_and_save(conversation, gen_message)
			response_get_gen = get_response(llm_get_gen, gen_message)
			while response_get_gen == -1:
				print("(truncating conversation)")
				llm_get_gen.pop(1)
				llm_get_gen.pop(1)
				llm_get_gen.pop(1)
				llm_get_gen.pop(1)
				time.sleep(30)
				response_get_gen = get_response(llm_get_gen, gen_message)
			content_get_gen = response_get_gen['choices'][0]['message']['content']
			print_and_save(conversation, content_get_gen)
			generalisation_empty = "FORMAL" in content_get_gen and len(content_get_gen.split("FORMAL")[1]) < 10
			gen_limit -= 1

		generalisation = content_get_gen.split("FORMAL")[1]

		while generalisation[0] in [":", "\n", " "]:
			generalisation = generalisation[1:]
		while generalisation[-1] in ["\n", " "]:
			generalisation = generalisation[:-1]
		if USING_CODE:
			generalisation = generalisation.split("```")[1].replace("python", "").replace("Python", "")
			# Sometimes the returned code leaves out the print part of template
			if "return" in generalisation.split("\n")[-1]:
				generalisation += "\n\nN = int(input(\"N=\"))\nconstraints = generate_constraints(N)\nconstraints = \", \".join(constraints)\nprint(constraints)"

	print_and_save(conversation, "(done with that example)")


	# Save this files conversation and statistics
	file_name = file_path.split("/")[-1][:-4]
	with open("saved_logs/"+file_name+"-log.txt", "w") as file:
		file.write("".join(conversation))
	experiment_stats[file_name] = convo_stats

	# Save individual statistics
	with open("individual_stats.json", "w") as file:
		json.dump(experiment_stats, file)

# Save overall statistics
overall_stats = {
	"succeeded": 0,
	"failed": 0,
	"average_attempts": 0,
	"max_attempts": MAX_ATTEMPTS,
	"average_examples_right": 0,
	"max_examples_right": MAX_EXAMPLES,
}
for key, value in experiment_stats.items():
	overall_stats["succeeded"] += 1 if value["succeeded"] else 0
	overall_stats["failed"] += 0 if value["succeeded"] else 1
	overall_stats["average_attempts"] += value["attempts"]
	overall_stats["average_examples_right"] += value["examples_right"]
overall_stats["average_attempts"] /= len(csv_files)
overall_stats["average_examples_right"] /= len(csv_files)
with open("overall_stats.json", "w") as file:
	json.dump(overall_stats, file)