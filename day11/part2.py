
test = """ghijklmn"""


def parser(data):
    return data

def main(data):
    data = parser(data)
    password = Password(data)
    
class Password:

    def __init__(self,data):
        self.data = (data.lower())
        self.alpha = "abcdefghijklmnopqrstuvwxyz"
        self.straight = tuple([self.alpha[i:i + 3] for i in range(len(self.alpha) - 2)])
        self.pairs = tuple([ i + i for i in self.alpha])
        # print(self.straight)
        self.change = 1
      
  


        self.check()
        self.add(1)
        self.check()

        # print(self.is_vaild())
      
        

    


 

    

    def convert(self,get = None):
        for i in range(len(self.data)):
            tmp = self.data[i]
            if type(self.data[i]) == int:
                get = True
                self.data[i] = self.alpha[self.data[i] - 1]
                
            else:
                self.data = list(self.data)            
                self.data[i] = self.alpha.find(tmp) + 1
        if get:
            self.data = "".join(self.data)
    def display(self):
        if type(self.data[0]) == int:
            self.convert()
            print(self.data)
            self.convert()
        else:
            print("".join(self.data))
    
    def check(self):
        a = 0
        while not self.is_vaild():
            self.add(self.change)
            a += 1
            if a % 100 == 0:
                pass
                # print(self.display())

        self.display()


    
    def add(self,no):
        if type(self.data[0]) != int:
            self.convert()
        pos = -1
        
        while no:
            val = self.data[pos]
            new_val = (val + no)
            if new_val > 26:
                no -= 26 - val
                new_val = new_val % 26
            else: 
                no = 0
            self.data[pos] = new_val
            pos -= 1
            if abs(pos) > len(self.data) and no != 0:
                self.data.insert(0,0)
 
    def is_vaild(self):
        if type(self.data[0]) == int:
            self.convert()

        for i in "iol":            
            if i in self.data:
                self.change = 1
                # print("bad present")

                return False
        self.change = 1

        
        for i in self.straight:
            # print(i,self.data)

            if i in  self.data:
                break
        else:
            # print("no stright")

            return False

        unique = None
        for i in self.pairs:
            if i in self.data:
                if unique == None:
                    unique = i
                elif unique != i:
                    return True
        # print("no aa occure")
        return False







    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

