
test = """^>v<"""
test = "^v"
test ="^v^v^v^v^v"

def parser(data):
    return data
def move(data,startlist = []):
    x = y = 0
    allplaces = startlist
    cc = 0

    for i in range(0,len(data)):
        
        
        match data[i]:
            case "^":
                y += 1
            case ">":
                x += 1
            case "<":
                x -=1
            case "v":
                y -=1


        if (x,y) not in allplaces:
            allplaces.append((x,y))
            cc += 1
    print(startlist)
        

    return cc,startlist

def main(data):
    data = parser(data)
    santa = data[::2]
    robo = data[1::2]
    print(santa,robo)

    a,ss = move(santa,[(0,0)])
    
    b,sb= move(robo,ss)
    print( a+b +1 )
    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)



"""

101010101

1000
1111
"""