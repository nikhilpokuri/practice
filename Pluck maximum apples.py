def apple(s):
    res=min(s)*len(s)
    for i in range(len(s)):
        temp=0
        for j in range(i,len(s)):
            if s[i]>s[j]:
                #print("yes")TO DEBUG
                break
            else:
                temp+=s[i]
                #print(temp) TO DEBUG
        res=max(res,temp)
    print(res)
n=int(input())
s=list(map(int,input().split()[:n]))
apple(s)
