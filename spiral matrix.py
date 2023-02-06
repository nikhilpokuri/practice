#spiral matrix
matrix=[]
row=int(input('row:'))
col=int(input('col:'))
for r in range(row):
    sub=[]
    for c in range(col):
        ele=int(input())
        sub.append(ele)
    matrix.append(sub)
#TO PRINT MATRIX
for k in matrix:
    print(*k)
print()

top=0
down=row-1
left=0
right=col-1
direc=0
while top<=down and left<=right:
    if direc==0:
        for i in range(left,right+1):
            print(matrix[top][i],end=" ")
        top+=1
    if direc==1:
        for i in range(top,down+1):
            print(matrix[i][right],end=" ")
        right-=1
    if direc==2:
        for i in range(right,left-1,-1):
            print(matrix[down][i],end=" ")
        down-=1
    if direc==3:
        for i in range(down,top-1,-1):
            print(matrix[i][left],end=" ")
        left+=1
    direc=(direc+1)%4#to make the directions repeat in [0,1,2,3] order
