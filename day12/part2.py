
test = """[1,{"c":"red","b":2},3]"""


def parser(data):
    return eval(data)

def main(data):
    data = parser(data)
    read = Reader(data)
    
class Reader:
    def __init__(self,data):
        self.data = data
        self.total = 0
        self.getnumbers(self.data)
        print(self.total)
       

    def getnumbers(self,data):
    
        if type(data) == list:
         
            
            for i in data:
                if type(i) == int:
                    self.total += i
                else:
                    self.getnumbers(i)
        elif type(data) == dict:
            if "red" in data.values():
                return 0
            
            for val in data.values():
                if type(val) == int:
                    self.total += val
                else:
                    self.getnumbers(val)




        



with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

