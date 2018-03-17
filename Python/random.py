def summary():

    name=(input("Please enter your name: "))
    age=int(input("Please enter your age: "))
    diff=100-age
    print("years to live: {0}".format(diff))

def difference(x,y):

    return(x-y)

def padovan():

    a=1
    b=1
    c=1
    while a<1000:
        print(a)
        a,b,c=b,c,a+b

def collinear():

    i=0
    l=[]
    l1=[]
    while (i<3):
        coord1,coord2=map(float,input("Enter a range: ").split(","))
        l.append(coord1)
        l.append(coord2)
        i+=1
    
    avg2=(coord2(i)/3)
    return (avg1,avg2)
    
def fourd():
    from random import randint
    a=0
    while(a<4):
        print(randint(1,49))
        a+=1

def pip():
    import telepot

def tree():
    t = [[[7], 1, [9]], 3, [[8], 2, [4]]]
    if len(t) == 1:
        return 1;
    else:
        return (len(t))
    
