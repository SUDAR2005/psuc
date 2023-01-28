#Write a python script to print left hill pattern
def leftHill(row):
    for i in range(1,row+1):
        for j in range(1,row+1):
            if i+j>row:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        for j in range(1,row):
            if j>=i:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print()
leftHill(20)