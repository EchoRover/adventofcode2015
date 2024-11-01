
test = """ugknbfddgicrmopn"""


def parser(data):
    
    return data.split("\n")
def nice(line):

    for i in ("ab", "cd", "pq", "xy"):
        if i in line:
            return False,"rule1"
    vowels = "aeiou"
    count = 0
    for i in line:
        if i in vowels:
            count += 1
    if count < 3:
        return False,"rule2"
    
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            return True,"ss"
    return False,"rule3"

    
    
def main(data):
    data = parser(data)
    niceC = 0
    for line in data:
        if nice(line)[0]:
            niceC += 1
        else:
            pass
            
    print(niceC)

    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

