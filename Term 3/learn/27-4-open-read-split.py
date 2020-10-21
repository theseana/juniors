with open('names.txt', 'r') as file:
    text = file.read()
text = text.split("\n")
print(text)