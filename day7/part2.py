
test = """123 -> x
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
456 -> y"""


def parser(data):
    data = data.split("\n")
    data = [lst.split() for lst in data]
    return data

def main(data):
    data = parser(data)
    cicuit = Circuit(data)




class Circuit:
    def __init__(self,data):
        self.copy = [lst.copy() for lst in data]
        self.var = {}
        self.a = None
        self.data = data

        self.runlines()        
        self.a = self.var["a"]
        self.var = {"b":self.a}
        self.data = self.copy
    
        # print(self.data)

        self.runlines()
        print(self.var["a"])
    
    def interpretLine(self,line):
        if len(line) == 3:
            if line[-1] == "b" and self.a != None:
                return

            a = int(line[0]) if line[0].isdigit() else self.var[line[0]]
            self.var[line[-1]] = a
        elif len(line) == 5:
            a,b = line[0],line[2]
            a = int(a) if a.isdigit() else self.var[a]
            b = int(b) if b.isdigit() else self.var[b]
            # print(a&b)
            # print(bin(a).strip("0b") & bin(b).strip("0b"))
        

            
                
            match line[1]:
                case "AND":
                    
                    self.var[line[-1]] = a & b 
                case "OR":
                    self.var[line[-1]] = a | b 
                case "LSHIFT":
                    self.var[line[-1]] = a << b 
                case "RSHIFT":
                    self.var[line[-1]] = a >> b

        elif len(line) == 4:
            a = line[1]
            a = int(a) if a.isdigit() else self.var[a]
            self.var[line[-1]] = 65535 - a
    
    def runlines(self):
       
        while self.data != []:
            
            try:
                a = self.data.pop()
                self.interpretLine(a)
                
                    
            except:
                self.data.insert(0,a)
                
                # backlog.append(line)


     
      


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

