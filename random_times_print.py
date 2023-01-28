#Write a program to  generate a random number andf print my name that many times
import random as r
i=0
while i<2:
    num=r.randint(1,10)
    i+=1
print(f"The number is {num}")
x=input("Enter your name:\t")
print(x*num)