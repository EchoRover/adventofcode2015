
test = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""


def parser(data):
    data = [lst.split() for lst in data.split("\n")]
    data = {(lst[0],lst[2]): int(lst[-1]) for lst in data}
    return data



def main(data):
    data = parser(data)
    planer = Planner(data)
    
class Planner:

    def __init__(self,data):
        self.dists = data
        self.places = set()
        self.longest = float('-inf')
        for i in self.dists.keys():
            self.places.add(i[0])
            self.places.add(i[1])
        self.connections = {key:[] for key in self.places}
        for place in self.connections:
            for i,j in self.dists:
                if place  == i:
                    self.connections[place].append(j)
                elif place == j:
                    self.connections[place].append(i)
        N = {}
        for key in self.dists:
            N[key[::-1]] = self.dists[key]
        self.dists.update(N)
        print(self.places,self.connections)

        self.travel()
    

    def travel(self):

        for start in self.places:
            self.gopath(start,list(self.places.copy()),0)
        
        print(self.longest)
    

    def gopath(self,node,travel,dist):

        travel.remove(node)
     


      


        if len(travel) == 0:
            self.longest = max(self.longest,dist)
    
       
        
        for connection in self.connections[node]:
            if connection in travel:
                self.gopath(connection,travel.copy(),dist + self.dists[(node,connection)])

        


    



with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

