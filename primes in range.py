import math
class Solution:
    def isprime(self,s):
        cou=0
        if s==2:
            return 1
        if s<2 or s%2==0:
            return 0
        for i in range(3,int(math.sqrt(s)+1),2):
            if s%i==0:
               return 0
        return 1
    def primeRange(self,M,N):
        res=[]
        for i in range(M,N+1):
            if self.isprime(i)==1:
                res.append(i)
        print(res)
s=Solution()
s.primeRange(1,10)
