#Write a program to print the sum of given matrix by getting input from user

def showMatrix(r,c):
    m =[]
    for i in range(r):
        l =[]
        for j in range(c):
            a=int(input(f"Enter element{i}{j}:\n"))
            l.append(a)
        m.append(l)
    return(m)
def sumMatrix(Mat_1,Mat_2):
    M_1 = []
    if len(Mat_1)>=len(Mat_2):
        a = len(Mat_2)
    else:
        a = len(Mat_1)
    for i in range(a):
        l_1 =[]
        if len(Mat_1[i])>len(Mat_2[i]):
            b = len(Mat_2[i])
        else:
            b = len(Mat_1[i])
            for j in range(b):
                Sum = Mat_1[i][j]+Mat_2[i][j]
                l_1.append(Sum)
            M_1.append(l_1)
    return M_1

r_1 = int(input("Enter the row 1:\n"))
c_1 = int(input("Enter the column 1:\n"))
mat_1 = (showMatrix(r_1,c_1))
r_2 = int(input("Enter the row 2:\n"))
c_2 = int(input("Enter the column 2:\n"))
mat_2 = (showMatrix(r_2,c_2))
print(sumMatrix(mat_1,mat_2))