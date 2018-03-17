word=input("Please enter a word: ")
search = sorted(word)
sortStr = ''.join(search)
print (sortStr)
with open("word.txt") as myFile:
    for line in myFile:
        line.sort
        newline = ''.join(line)
        if (newline == sortStr and newline[0]=='v'):
            print(line)

