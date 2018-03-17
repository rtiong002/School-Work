password = input("Please input password: ")
uppC = False
lowC = False
num = False
length = False

for c in password:
    if c.isupper():
        uppC = True
    if c.islower():
        lowC = True
    if c.isdigit():
        num = True
length = len(password)>8

print((uppC and lowC and num and length))
