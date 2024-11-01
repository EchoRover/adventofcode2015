
test = """^>v<"""


def parser(data):
    return data
def move(data):
    x = y = 0
    allplaces = []

    for i in data:
        if (x,y) not in allplaces:
            allplaces.append((x,y))
        match i:
            case "^":
                y += 1
            case ">":
                x += 1
            case "<":
                x -=1
            case "v":
                y -=1
    return len(allplaces)
def main(data):
    data = parser(data)

    print(move(data))
    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

