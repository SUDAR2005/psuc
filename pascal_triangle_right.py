#Write a program to print a pascal triangle facing left
r = int(input("Enter the number of rows:\n"))
for i in range(r):
    for j in range(r):
        if i>j:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()