with open('names.txt', 'r') as file:
    while True:
        
        line = file.readline()
        print(line)
        if line == "":
            break
        
print("Something Breaked!")