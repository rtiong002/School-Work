def range():

    a = int(input("Please enter value a: "))
    b = int(input("Please enter value b: "))
    c = int(input("Please enter value c: "))

    largest = a
    smallest = a

    if (b>largest):
        largest = b
    else:
        smallest = b
    if (c>largest):
        largest = c
    elif (c<smallest):
        smallest = c

    diff=largest-smallest
    print(" Largest: {0} \n Smallest: {1} \n Range: {2}".format(largest,smallest,diff))

    #Second method, less comparison
    if (a>b):
        if (c<b):
            diff=abs(a-c)
        else:
            diff=abs(a-b)
    else:
        diff=abs(b-c)
    
