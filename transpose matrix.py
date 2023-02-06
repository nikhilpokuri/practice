#transpose of matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("TRANSPOSED matrix")
for i in range(len(matrix)):
    tran=[]
    for j in range(len(matrix)):
        tran.append(matrix[j][i])
    print(*tran)
