def formatIdentityMat(row=1,a=int(1)):
    IDmat=[]
    for i in range(row):
        colID=[]
        for j in range(row):
            if i==j:
                colID.append(a)
            else:
                colID.append(0)
        IDmat.append(colID)
    return (IDmat)
a = formatIdentityMat(3,4)
b=a+[[1,1,1],[1,2,3],[3,5,4]]
def findIdentityMatrix(mat):
    for i in range(len(mat)):
        if len(mat)!=len(mat[i]):
             return False
    for j in range(len(mat)-1):
        if mat[j][j]!=mat[j+1][j+1] :
             return False
    for k in range(len(mat)):
        for i in range(len(mat[0])):
            if mat[k][i]!=0 and i!=k:
                return False
    return True
print(findIdentityMatrix(a))
print(findIdentityMatrix(b))