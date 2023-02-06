def isprime(num):
    cnt=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            cnt+=1
    if cnt>1:
        return False
    return True
def primes(num):
    prim=0
    for j in range(2,num):
        s=isprime(j)
        if s:
            prim=prim+j
    if prim%num==0:
        return True
    return False
#DRIVER CODE
s=primes(5)
print(s)

