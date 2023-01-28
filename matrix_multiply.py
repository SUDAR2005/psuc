#Python script to multiply  matrix
def mat_generation(row,col):
    mat = []
    for i in range(row):
        mat_row = []
        for j in range(col):
            a=int(input(f"Enter the Element{i+1}{j+1}:"))
            mat_row.append(a)
        mat.append(mat_row)
    return mat
def mat_multiply(mat1,mat2):
    result = []
    for i in range(len(mat1)):
        res_row = []
        for j in range(len(mat2[0])):
            res_row.append(0)
        result.append(res_row)
    if len(mat1[0])==len(mat2):
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(result)):
                    result[i][j]+=mat1[i][k]*mat2[k][j]
        return result
def Transpose(mat):
    trans=[]
    for i in range(len(mat)):
        trans_row=[]
        for j in range(len(mat[0])):
            a=mat[j][i]
            trans_row.append(a)
        trans.append(trans_row)
    return trans
def findSecDiagonal(mat):
    sum=0
    for i in range(len(mat)):
        sum+=mat[i][len(mat)-1]
    return sum
matrix=mat_generation(3,3)
print(findSecDiagonal(matrix))
Matrix=mat_generation(2,2)
print(mat_multiply(matrix,Matrix))
print(Transpose(matrix))
