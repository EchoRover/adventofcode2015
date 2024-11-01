
test = """turn on 0,0 through 9,9
turn on 0,0 through 9,9
toggle 0,0 through 4,4"""


def parser(data):
    data = data.split("\n")
    data = [lst.split() for lst in data]
   
    data = [[lst[1],tuple(map(int,lst[2].split(","))),tuple(map(int,lst[-1].split(",")))] if len(lst) == 5 else [lst[0],tuple(map(int,lst[1].split(","))),tuple(map(int,lst[3].split(",")))]  for lst in data]

    return data


class Lights:
    def __init__(self,leng,bre,data):
        self.data = data
        self.len = leng
        self.bre = bre
        self.grid = [[0 for i in range(self.len)] for j in range(self.bre)] 
        self.lightslit()
     

        self.doinstructions()
        self.lightslit()
        # self.display()

     
    
    def lightslit(self):
        c = 0
        for y in self.grid:
            c += y.count(1)
        print(c)

    def display(self):
        f = open("view.txt","w")
        for y in self.grid:
            print("".join(map(str,y)))
            f.write("".join(map(str,y)))
        f.close()
        

    def doinstructions(self):
        for line in self.data:
           
        
            if line[0] == "on":
                self.switch(line[1],line[2],1)
            elif line[0] == "off":
                self.switch(line[1],line[2],0)
            else:
                self.toggle(line[1],line[2])


    
    def switch(self,p1,p2,state):
        for x in range(p1[0],p2[0] + 1):
            for y in range(p1[1],p2[1] + 1):
                self.grid[y][x] = state

    def toggle(self,p1,p2):
        
        for x in range(p1[0],p2[0] + 1):
            for y in range(p1[1],p2[1] + 1):
                self.grid[y][x] = 1 if self.grid[y][x] == 0 else 0
    



def main(data):
    data = parser(data)
    
    lights = Lights(1000,1000,data)


    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

