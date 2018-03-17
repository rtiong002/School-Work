def prob1():
    print('.'.join([x[0] for x in input("Enter your name:").split()])+'.')

def prob2():
    num = input("Please enter a series of single-digit numbers without space for summation: ")
    separate = []
    for i in num:
        separate.append(i)
    separate = map(int,separate)
    print('{:>10d}'.format(sum(separate)))

def prob3():
    date1 = input("Please enter date(dd/mm/yyyy): ")
    date2 = ''.join(date1).split('/')
    if date2[1]=='01':
        month = 'January'
    elif date2[1]=='02':
        month = 'February'
    elif date2[1]=='03':
        month = 'March'
    elif date2[1]=='04':
        month = 'April'
    elif date2[1]=='05':
        month = 'May'
    elif date2[1]=='06':
        month = 'June'
    elif date2[1]=='07':
        month = 'July'
    elif date2[1]=='08':
        month = 'August'
    elif date2[1]=='09':
        month = 'September'
    elif date2[1]=='10':
        month = 'October'
    elif date2[1]=='11':
        month = 'November'
    elif date2[1]=='12':
        month = 'December'
    date3 = date2[0],month,',',date2[2]
    
    print(' '.join(date3))
    
    
