#Python script to print heart pattern using function
def butterflyPattern(r):
    for i in range(1,r+1):
        for j in range(1,r+1):
            if i>=j and (i+j!=2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        for j in range(1,r+1):
            if i+j>r and ((j!=r-1 or j!=r) and (i!=1)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    for i in range(1,r+1):
        for j in range(1,r+1):
            if i+j>r+1 or (i==r and j==1):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        for j in range(1,r+1):
            if i>j or (i==r and j==r):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print()
str(butterflyPattern(10))