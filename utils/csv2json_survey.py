import re
import json

file = open("survey.txt", "r", encoding='utf-8')
json_data = {}
json_data['survey'] = []
category_set = []

while True:
	line = file.readline()
	if not line:
		break
	data = re.split(r'\t+', line.rstrip())
	data[0] = data[0].replace(" ", "_")
	# data[1] = data[1].replace(" ", "_")
	if data[0] in category_set:
		i = [item for item in json_data['survey'] if item['category'] == data[0]]
		statement = {}
		statement['question'] = data[1]
		statement['frequency'] = 0
		statement['strength'] = 0
		i[0]['statement'].append(statement)
	else:
		temp = []
		statement = {}
		statement['question'] = data[1]
		statement['frequency'] = 0
		statement['strength'] = 0
		temp.append(statement)
		json_data['survey'].append({'category': data[0], 'statement': temp})
		category_set.append(data[0])

file.close()

with open('survey.json', 'w') as outfile:
    json.dump(json_data, outfile, ensure_ascii=False, indent=4, skipkeys=True)