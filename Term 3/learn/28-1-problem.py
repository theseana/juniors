with open('new.txt', 'w') as output:
    with open('dataset.bat', 'r') as dataset:
        while True:
            line = dataset.readline()
            if line.startswith("wget"):
                output.write(line.split()[3].strip("'")+"\n")
            if line == "":
                break