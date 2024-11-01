
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
        simpletxt = line[1:-1]
     
        simpletxt = simpletxt.replace("""\\\\""","""\\""")
        simpletxt = simpletxt.replace('\\"',"\"")
        # print(line,simpletxt)
        

        count = 0
        for idx,i in enumerate(simpletxt):
    
            if i == "x":
                if idx - 1 >= 0 and simpletxt[idx - 1] == "\\":
                    try:
                        if simpletxt[idx + 1].lower() in "1234567890abcdef" and simpletxt[idx + 2].lower() in "1234567890abcdef": 
                            count -= 2
                        else:
                            count += 1
                    except:
                        count += 1
                
                else:
                    count += 1
                
            else:
                count += 1
            # print(i,count)
            


        self.strno += count
       

        
    
    def solveall(self):
        for line in self.data:
            self.readline(line)

            if self.data.index(line) > 10:
                pass 
            
            
        

        print(self.strno,self.codeno)
        print(self.codeno - self.strno)

with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

