# "FIBBONACCI_SERIES"
num=int(input())
n1=0
n2=1
fib=[n2]
for i in range(num-1):
    n3=n1+n2
    fib.append(n3)
    n1=n2
    n2=n3
print(fib)
