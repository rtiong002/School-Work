def qn1():
    grades ={
        'FS1' : [(1,45),(2,65),(3,75)],
        'FS2' : [(1,45),(2,75),(3,65)]
        }

    grades2 = {
        ('FS1',1):45,('FS1',2):65,}

def qn2():
    a=[]
    x=int(input("Please enter marks for class A. When done enter -1. "))
    while x!=-1:
        a.append(x)
        x=int(input("Please enter marks for class A. When done enter -1. "))
    

    b=[]
    y=int(input("Please enter marks for class B. When done enter -1. "))
    while y!=-1:
        b.append(y)
        y=int(input("Please enter marks for class B. When done enter -1. "))

    avga = float(sum(a))/len(a)
    avgb = float(sum(b))/len(b)

    amax = max(a)
    bmax = max(b)    
    
    if (amax>bmax):
        print("A class has the higher maximum score of ",amax)
    else:
        print("B class has the higher maximum score of ",bmax)

    if (avga>avgb):
        print("A class has the higher average score of ",avga)
    else:
        print("B class has the higher average score of ",avgb)

    print ("A class " + a)
    print ("B class " + b)
    
        
def qn3():
    for x in range(1,101):
    if (x**2%3)==0:
        print (x**2)

    print((x**2 for x in range (1,101) if x%3==0)
