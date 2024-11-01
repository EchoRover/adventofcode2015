
test = """{"a":{"b":4},"c":-1}"""


def parser(data):
    return data

def main(data):
    data = parser(data)
    read = Reader(data)
    
class Reader:
    def __init__(self,data):
        self.data = data
        self.getnumbers()

    def getnumbers(self):
        total = 0

        no = ""
        for i in  self.data:
            if i .isdigit() or i == "-":
                no += i
            else:
                if no != "":
                    total += int(no)
                no = "" 
        print(total)


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

