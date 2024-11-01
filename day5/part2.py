
test = """qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy"""


def parser(data):
    
    return data.split("\n")
def nice(line):

    for i in range(len(line)- 2):
        if line[i] == line[i + 2]:
            break
    else:
        return False,"rule1"
    for i in range(len(line) - 1):
        sub = line[i:i + 2]
        if line.count(sub) >= 2:
            return True,"ss"
    return False,"rule2"
    


    
    
def main(data):
    data = parser(data)
    niceC = 0
    for line in data:
        if nice(line)[0]:
            niceC += 1
        else:
            continue
            print(nice(line),line)
            
    print(niceC)

    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

