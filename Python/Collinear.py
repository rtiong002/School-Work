import math
def collinear():    
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))

    a = ((y2-y1)*(x3-x1))
    b = ((y3-y1)*(x2-x1))

    if a == b:
        print("Coordinates are collinear.")
    else:
        print("Coordinates are not collinear.")

        
