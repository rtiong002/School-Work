def qn1():
    max_score=0
    min_score=100
    print("note: enter -1 to end")
    score = int(input("Please enter score: "))
    while True:
        if score==-1:
            break
        if score>max_score and score<=100:
            max_score=score
        elif score<min_score and score>=0:
            min_score=score    
        if score>=80 and score<=100:
            print("grade: A")
        elif score<80 and score>=60:
            print("grade: B")
        elif score<60 and score>=40:
            print("grade: C")
        elif score<40 and score>=0:
            print("grade: F")
        score = int(input("Please enter score: "))
    print("max_score = {}".format(max_score))
    print("min_score = {}".format(min_score))   
    
    
        
def qn2():
    n=int(input("Enter variable n: "))
    count=1
    while count<n:
        print(count*"*")
        count+=1
    while count>0:
        print(count*"*")
        count-=1

    
