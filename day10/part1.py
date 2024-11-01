
test = """1"""


def parser(data):
    return data

def main(data):
    data = parser(data)

    for _ in range(40):
        data = process(data)
    print(len(data))


    

def process(data):
    count = 0
    current = data[0]
    final = ""
    for i in data:
        if i != current:
            final += str(count) + current
            count = 0
            current = i
        count += 1
    final += str(count) + current
    return(final)
    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

