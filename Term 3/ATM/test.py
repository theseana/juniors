import json

with open('names.json', 'r') as file:
    file_json =json.dumps(file, indent=2)

print(file_json)