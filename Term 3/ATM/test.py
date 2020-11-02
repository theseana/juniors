import json

with open('names.json') as file:
    file_json =json.load(file)
    data = {"username": "mahdi", "password": "mannamaman"}     
    file_json.append(data)

 

with open('names.json', 'w', encoding='utf-8') as file:
    json.dump(file_json, file, ensure_ascii=False, indent=4)
