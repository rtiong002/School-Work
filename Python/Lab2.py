import math

def prob1():
    r=int(input("Please input radius: "))
    v=(4/3)*math.pi*(r**3)
    a=4*math.pi*(r**2)

    print("Volume is {0} and surface area is {1}".format(v,a))

def prob2():
    a1=int(input("a1: "))
    b1=int(input("b1: "))
    c1=int(input("c1: "))
    a2=int(input("a2: "))
    b2=int(input("b2: "))
    c2=int(input("c2: "))
    base=(a1*b2)-(a2*b1)

    if(base==0):
        print("Unable to compute as base is 0")
    else:
        x=((b2*c1)-(b1*c2))/base
        y=((a1*c2)-(a2*c1))/base
    print("x = ",x)
    print("y = ",y)

def prob3():
    print("please input birthday of 1st person")
    y1=int(input("year: "))
    m1=int(input("month: "))
    d1=int(input("day: "))
    print("please input birthday of 2nd person")
    y2=int(input("year: "))
    m2=int(input("month: "))
    d2=int(input("day: "))
    print((y1<y2) or (y1==y2 and ((m1<m2) or m1==m2 and(d1<d2))))
