import random
num=random.randint(1,10)
i=0
while i<5:
    ans=int(input("number thingy : "))
    if ans == num:
        print("yes yes yes yes")
        print(num)
        e=int(input("How many times did it take you to finish"))
        if e >= 10:
            print("bruh")
        if e <=10:
            print("ez dubs")
        break

    if num >= ans:
        print("too low")
        num=random.randint(1,10)
    
    if num <= ans:
        print("too high")
        num=random.randint(1,10)
    i=i+1