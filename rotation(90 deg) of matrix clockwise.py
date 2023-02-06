matrix=[]
size=int(input())
for row in range(size):
    sub=[]
    for col in range(size):
        ele=int(input())
        sub.append(ele)
    matrix.append(sub)
#TO PRINT BEFORE ROTATING MATRIX
for k in matrix:
    print(*k)
print()
#TO PRINT AFTER ROTATING 90 DEGREES CLOCKWISE MATRIX
for i in range(3):
    j=2
    while j!=-1:
       print(matrix[j][i],end=" ")
       j-=1
    print()
