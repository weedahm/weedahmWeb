import re, json

file = open("survey.txt", "r")
json_data = {}
json_data['survey'] = []
while True:
	line = file.readline()
	if not line: break
	data = re.split(r'\t+', line.rstrip())
	json_data['survey'].append({
		'category': data[0],
		'statement': data[1]
	})
file.close()

with open('survey.json', 'w') as outfile:
	json.dump(json_data, outfile)