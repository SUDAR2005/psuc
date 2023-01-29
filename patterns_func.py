#Python script to generate patterns
def rightTriangle(row):
    for i in range(1,row+1):
        for j in range(i):
            print("*",end=" ")
        print()
def mirrorRightTriangle(row):
    for i in range(1,row+1):
        for j in range(row-i):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
def mirrorRightTriangle2(row):
    for i in range(1,row+1):
        for j in range(1,row+1):
            if i+j<row+1:               #Can either use i+j<=row
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print()
def invertTriangle(row):
    for i in range(1,row+1):
        for j in range(row+1-i):
            if i+j<row+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def mirrorInvertedTriangle(row):
    for i in range(1,row+1):
        for j in range(1,row+1):
            if i>j:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print()
def Equilateraltriangle(row):
    k = row
    for i in range(1,row+1):
        for j in range(k):
            print(end=" ")
        k = k - 1
        for j in range(i):
            print("* ", end="")
        print()