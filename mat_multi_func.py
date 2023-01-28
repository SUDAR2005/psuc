#Write a python program to do multiplication of matrix
def formatMatrix(rows=int(),col=int()):
    l=[]
    for i in range(rows):
        l_1=[]
        for j in range(col):
            a=int(input(f"Enter element[{i}][{j}]:"))
            l_1.append(a)
        l.append(l_1)
    return l
def multiplyMatrix(mat1=list(),mat2=list()):
    result=[]
#To check matrix multiplicity
    if len(mat1[0])!=len(mat2):
        raise Exception("The given matrix can't be multiplied")
        quit()
#To print result block
    for i in range(len(mat1)):
        res_row=[]
        for j in range(len(mat2[0])):
            res_row.append(0)
        result.append(res_row)
#To append matrix using main logic
    for i in range(len(mat1)):              #interates the no of times as rows in mat1
        for j in range(len(mat2[0])):       #interates the no of times as columns in mat2
            for k in range(len(result)):    #Interrates the number of times the rows in result
                result[i][j]+=mat1[i][k]*mat2[k][j]
    return result
m=formatMatrix(2,3)
n=formatMatrix(3,7)
print(multiplyMatrix(m,n))