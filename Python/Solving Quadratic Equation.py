def quad():
    from math import sqrt
    print ("Calculate the value of x for ax^2 + bx + c")
    print()
    a = int(input("Please enter integer a: "))
    b = int(input("Please enter integer b: "))
    c = int(input("Please enter integer c: "))

    d = b**2 - 4*a*c
    disc = sqrt(d)
    positive = (-b + disc)/(2*a)
    negative = (-b - disc)/(2*a)

    if positive == negative:
        print ("The value of x is {0}".format(positive))
    else:
        print ("The value of x is {0} and {1}".format(positive,negative))
    
        
    

    

