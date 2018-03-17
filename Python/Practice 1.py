num = int(input("Please enter number: "))

for y in range(num):
    for x in range(num):
        if(x<=y):
            print('#',end='')
        else:
            print(' ',end='')
    print()
for y in range(num-2):
    for x in range(num):
        if (x==0 or x==(num-1)):
            print('#',end='')
        else:
            print(' ',end='')
    print()
for y in range(num):
    for x in range(num):
        if(x>=y):
            print('#',end='')
        else:
            print(' ',end='')
    print()
