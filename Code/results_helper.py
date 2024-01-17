import json

# Save overall statistics
overall_stats = {
	"succeeded": 0,
	"attempts": 0,
	"examples_right": 0
}

with open("individual_stats.json", "r") as file:
	experiment_stats = json.load(file)

length = 0
for key1, value1 in experiment_stats.items():
	length += 1
	for key2,value2 in value1.items():
		overall_stats[key2] += value2
for key in overall_stats.keys():
	if key == "succeeded":
		continue
	overall_stats[key] /= length
overall_stats["max_attempts"] = 10
overall_stats["max_examples"] = 10
overall_stats["failed"] = length - overall_stats["succeeded"]
with open("overall_stats.json", "w") as file:
	json.dump(overall_stats, file)