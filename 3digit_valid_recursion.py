#Write a python script to print a random three digit number
import random as r
def formDigits(n=int()):
    num=""
    for i in range(n):
        num+=str(r.randrange(1,9))
    return int(num)
print(formDigits(7))