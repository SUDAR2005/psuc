#Write a python program to print collection of patterns
from math import factorial as f
def pattern1(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
print("\n")
pattern1(5)

def pattern2(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
print("\n")
pattern2(5)

def pattern3(row):
    for i in range(1,row+1):
        for j in range(row+1,i,-1):
            print(i,end=" ")
        print()
print("\n")
pattern3(5)

def pattern4(row):
    for i in range(row,0,-1):
        for j in range(i+1):
            print(j,end=" ")
        print()
print("\n")
pattern4(5)

def pattern5(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(i*2-1,end=" ")
        print()
print("\n")
pattern5(5)

def factTTree(row):
    for i in range(row):
        for j in range(row-i+1):
            print(" ",end=" ")
        print()
        for j in range(i-1):
            print(f(i)//f(j)*f(i-j),end=" ")
        print()
factTTree(5)