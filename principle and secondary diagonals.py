#diagonals of matrix
matrix=[[1,2,3],[4,5,6,],[7,8,9]]
for i in matrix:
    print(i)
print("PRINCIPLE DIAGONAL matrix")
for i in range(len(matrix)):
    dig=[]
    for j in range(len(matrix)):
        if(i==j):
            dig.append(matrix[i][j])
    print(dig)
print("SECONDARY DIAGONAL matrix")
for i in range(len(matrix)):
    dig1=[]
    for j in range(len(matrix)):
        if(i+j==2):
          dig1.append(matrix[i][j])
    print(dig1)