
test = """()())()"""


def parser(data):
    return data
def solve(data):
    floor = 0
    for idx,i in enumerate(data):
        if i == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return idx + 1
    
def main(data):
    data = parser(data)
    print(solve(data))
    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

