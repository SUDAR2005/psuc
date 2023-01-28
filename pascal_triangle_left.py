#Write a program to print a left facing pascal triangle
r=int(input("Enter the number of rows:\n"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


