
test = """"""


def parser(data):
    data = data.split("\n")
    data = [list(map(int,i.split("x"))) for i in data]
    return data

def main(data):
    data = parser(data)
    area = 0

    for box in data:
        area += barea(box)
    print(area)
    
def barea(box):
    l,w,h = box
    a = 2 * l * w + 2*w*h + 2*h*l
    m1 = min(box)
    box.remove(m1)
    m2 = min(box)
    a += m1 * m2
    return a

with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

