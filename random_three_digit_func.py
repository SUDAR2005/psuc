#Write a program to print the random three digit number using func
import random as r
def randomNumber(n):
    s=""
    for i in range(n):
        a = r.randrange(1,9)
        s+=str(a)
    return s
num = int(input())
print(randomNumber(num))