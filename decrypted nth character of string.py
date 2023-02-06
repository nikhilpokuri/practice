def res(s,n):
    sub=""
    res=""
    for i in range(len(s)):
        if s[i].isalpha():
            sub+=s[i]
        else:
            res+=int(s[i])*sub
            sub=""
    print(res)
    if n<=len(s):
        print(res[n-1])
    else:
        print(-1)
string=input()#i/p=a3b3c3------->o/p=aaabbbccc
n=int(input())#5th character in above output string
res(string,n)










