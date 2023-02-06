#maximum sum of the sub array
arr=[1,2,3,-2,5]
sum_sub=0
Sum=arr[0]
for i in arr:
    sum_sub+=i
    Sum=max(Sum,sum_sub)
    if sum_sub<0:
        sum_sub=0
print(Sum)
#maximum of sum of these [1],[1,2],[1,2,3],[1,2,3,-2],[1,2,3,-2,5] sub arrays
