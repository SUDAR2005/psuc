def sumUpperLower(mat1):
    usum=0
    lsum=0
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if i>=j:
                usum+=mat1[i][j]
            elif i+j<=len(mat1)-1:
                lsum+=mat1[i][j]
    print(f"{usum}")
    print(f"{lsum}")
    print(f"{lsum+usum}")
sumUpperLower([[2,3,4],[1,2,3],[1,2,3]])
