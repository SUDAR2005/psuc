#Python script to print the pascal triangle and 1-121-12321 Pyramid pattern
from math import factorial as f
def pascalTriangle(row):
    for i in range(row):
        for j in range(row-i):
            print(end=" ")
        for j in range(i+1):
            print(int(f(i)/(f(j)*f(i-j))),end=" ")
        print()
def sumPyramid(row):
    for i in range(row):
        k=1
        for j in range(row):
            if i+j<row:
                print(" ",end=" ")
            else:
                print(k,end=" ")
                k+=1
        for j in range(i+1,0,-1):
            print(j,end=" ")
        print()
pascalTriangle(5)
sumPyramid(5)