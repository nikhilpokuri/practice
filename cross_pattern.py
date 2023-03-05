n = int(input('enter the odd number:'))
res = ''.join([str(i) for i in range(1,n+1)])
for i in range(n):
    for j in range(n):
        if (i == j) or (i+j == n-1):
            print(i+1,end = ' ')
        else:
            print(' ',end=' ')
    print()