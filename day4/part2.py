import hashlib
test = """abcdef"""


def parser(data):
    return data

def mine(data):
    no = 1
    result = hashlib.md5((data + str(no)).encode()).hexdigest()

    while not result.startswith("000000"):
        no += 1
        result = hashlib.md5((data + str(no)).encode()).hexdigest()

    return no

def main(data):
    data = parser(data)

    print(mine(data))


    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

