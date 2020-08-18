import random
num=random.randint(1,10)
print("please type a number e.g. 5")
i=012

while i<5
    ans=int(input("Number : "))
    if num == ans:
        print("You did it!")
        print(num)
        break
    elif num >= ans:
        print("too low")
        print(num)
        break
    elif num <= ans:
        print("too high")
        print(num)
        break