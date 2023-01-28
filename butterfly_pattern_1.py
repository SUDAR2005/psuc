#Print a butterfly pattern of given order
n = int(input("Enter half the number of rows:"))
for i in range(n):
    for j in range(n):                  #for upper left
        if j-i<1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):                  #for upper right
        if i+j+2>n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):                   #for lower left
        if j<n-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):                   #for lower right
        if i>j:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


