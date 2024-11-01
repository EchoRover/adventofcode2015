
test = open("day8/test.txt").read()


def parser(data):
    return data.split("\n")

def main(data):
    data = parser(data)

    analyze = Analyze(data)
    
class Analyze:

    def __init__(self,data):
        self.data = data
        self.strno = 0
        self.codeno = 0

        self.solveall()
    

    def readline(self,line):
        self.codeno += len(line)
 
        simpletxt = line.replace("\\","\\\\")
        simpletxt = simpletxt.replace('"','\\"')
        count = len(simpletxt)
        self.strno += count + 2
        # print(simpletxt,count + 2)
  
            


       

        
    
    def solveall(self):
        for line in self.data:
            self.readline(line)

            if self.data.index(line) > 10:
                pass 
            
            
        

        print(self.strno,self.codeno)
        print(self.strno - self.codeno)

with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

