import math

def pay():

    hour = float (input("Please enter number of hours worked: "))

    if (hour>160):
        gross = ((hour-160)*15)+(160*10)

    elif (hour<=0):
        print("Invalid input")
        return
        
    else:
        gross = hour*10

    if (gross>1500):
        tax = ((gross-1500)*0.3)+200

    elif (gross>1000):
        tax = ((gross-1000)*0.2)+100

    else:
        tax = gross*0.1

    net = gross - tax

    print(" gross pay is ${0},\n tax is ${1},\n net pay is ${2}".format(gross,tax,net))

