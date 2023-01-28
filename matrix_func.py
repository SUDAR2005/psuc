#Write a program to print the  matrix by getting input from user
def showmatrix(r,c):
    m =[]
    for i in range(r):
        l =[]
        for j in range(c):
            a = int(input())
            l.append(a)
        m.append(l)
    return m
r_1 = int(input("Enter the number of rows:\t"))
c_1 = int(input("Enter the number of column:\t"))
print(showmatrix(r_1,c_1))
