#Write a python script to find the uniqure diagonal elements
import random as r
def formatMatrix(row,col):
    mat=[]
    for i in range(row):
        mat_row=[]
        for j in range(col):
            a= r.randrange(1,10)
            mat_row.append(a)
        mat.append(mat_row)
    return(mat)
def checkRow(mat):
    for i in range(len(mat)):
        unique=1
        s=set()
        for j in range(len(mat[i])-1):
            if mat[i][j]!=mat[i][j+1]:
                unique+=1
                s.add(mat[i][j])
                s.add(mat[i][j+1])
        print("The number of unique elements",unique)
        print("The elements are",s)
    return 1

a=formatMatrix(3,4)
print(a)
checkRow(a)