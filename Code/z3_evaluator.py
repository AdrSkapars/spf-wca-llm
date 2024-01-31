import json
import subprocess

code_header = "from z3 import *\nN = Int('N')\nss = Function('ss', IntSort(), IntSort())\n\n########\n\n"
code_footer = "\n\n########\n\nprove(And(Implies(prediction, truth), Implies(truth, prediction)), random_seed=10)"

with open("individual_stats.json", "r") as jsonf:
	expected = json.load(jsonf)

target_programs = [
	"own.SameHundred",
	"own.SameLowercase",
	"own.SameOnlyThird",
	"own.SameString",
	"own.SimpleAscendingLast",
	"own.SimpleEveryThird",
	"own.SimpleSignFlip",
	"own.SimpleSymmetric",
	"own.SimpleTrueFalse",
	"own.SimpleUnique",
	"own.WeirdConstDiff",
	"own.WeirdFibonacci",
	"own.WeirdTimes",
	"own.BadgerHash",
	"own.BadgerPassword",
	"own.BadgerUsername",
	"own.ComplexFlipPos_1",
	"own.ComplexFlipPos_2",
	"own.ComplexHalfEqual",
	"own.ComplexMidPeak",
	"own.ComplexPalindrome",
	"own.ComplexOddsEvens",
]

stats = {
	"proved": 0,
	"countered": 0,
	"timedout": 0,
	"errored": 0,
	"proved_l": [],
	"countered_l": [],
	"timedout_l": [],
	"errored_l": [],
}


for tprogram in target_programs:

	prediction_path = "z3_generals/" + tprogram + ".py"
	with open(prediction_path, "r") as f:
		prediction = f.read()

	truth_path = "../Dataset/z3_annotations/" + tprogram + ".py"
	with open(truth_path, "r") as f:
		truth = f.read()

	code = code_header + prediction + "\n\n########\n\n" + truth + code_footer
	code_path = "z3_generals/runs/" + tprogram + ".py"
	with open(code_path, "w") as f:
		f.write(code)

	try:
		output = subprocess.run(["python3", code_path], text=True, capture_output=True, check=True, timeout=10)
		result = output.stdout
		if "proved" in result:
			print(tprogram, "proved")
			stats["proved"] += 1
			stats["proved_l"].append(tprogram)
		else:
			stats["countered"] += 1
			stats["countered_l"].append(tprogram)
			if expected[tprogram]["succeeded"] == False:
				print(tprogram, "skipped, expected to fail and it did")
			else:
				if tprogram not in ["own.SimpleSignFlip"]:
					print(tprogram, "didn't expect to fail but it did\n", result)
					break
	except subprocess.TimeoutExpired:
		stats["timedout"] += 1
		stats["timedout_l"].append(tprogram)
		if expected[tprogram]["succeeded"] == False:
			print(tprogram, "timed out, expected to fail")
		else:
			print(tprogram, "timed out, didn't expect to fail")		

	except subprocess.CalledProcessError as e:
		error = e.stderr
		print(tprogram, "errored\n", error)
		stats["errored"] += 1
		stats["errored_l"].append(tprogram)
		break

with open("z3_stats.json", "w") as file:
	json.dump(stats, file)

