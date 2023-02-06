#addition of matrixes
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    result=[]
    for j in range(len(b)):
        add=a[i][j]+b[i][j]
        result.append(add)
    print(result)
        
