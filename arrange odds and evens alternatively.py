N = int(input())
array = list(map(int,input().split(",")[:N]))
evens = sorted(list(filter(lambda a: a % 2 == 0, array)))
odds = sorted(list(filter(lambda a: a % 2 != 0, array)))

sol=list(zip(sorted(odds),sorted(evens)))#to pair each value of two arrays..,i.e (odd,even),(odd,even)...

#to convert the zipped tuples into single list
res=[]
for i in sol:
    res+=list(i)

#to add remaining
rem=[]
if len(evens)<len(odds):
    rem+=odds[len(evens):]
else:
    rem+=evens[len(odds):]
print(res+rem)
