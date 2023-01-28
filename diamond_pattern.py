#Write a python script to print the diamond pattern
def diamondPatter(row):
#for upper part of diamond
    for i in range(row):
        for j in range(i,row):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
#for lower part of diamond
    for i in range(row+1):
        for j in range(i):
            print(" ",end=" ")
        for j in range(i,row):
            print("*",end=" ")
        for j in range(i,row+1):
            print("*",end=" ")
        print()
diamondPatter(5)