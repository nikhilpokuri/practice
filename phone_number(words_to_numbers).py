s=input("Enter ur number in words:")
s=s.split()
res=[]
for i in s:
    if i=="one":
        res.append("1")
    elif i=="two":
        res.append("2")
    elif i=="three":
        res.append("3")
    elif i=="four":
        res.append("4")
    elif i=="five":
        res.append("5")
    elif i=="six":
        res.append("6")
    elif i=="seven":
        res.append("7")
    elif i=="eight":
        res.append("8")
    elif i=="nine":
        res.append("9")
    elif i=="zero":
        res.append("0")
    elif i=="double":
        res.append("double")
    elif i=="triple":
        res.append("triple")
for j in res:
    if j=="double":
        ind=s.index(j)
        res[ind]=res[ind+1]
    elif j=="triple":
        ind=s.index(j)
        res[ind]=2*res[ind+1]
s=""
for k in res:
    s=s+k
print(s)
