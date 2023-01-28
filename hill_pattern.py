#Write code to print hill pattern
r = int(input("Enter the number of rows:"))
for i in range(r):                                                #For left part of hill
    for j in range(r):
        if i+j<r-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    for j in range(r):
        if j+1<=i:                                                #For right part of hill
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
