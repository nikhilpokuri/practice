nums=[1,4,3,2,6]
sort_arr=sorted(nums)#[1,2,3,4]
cnt=0
for i in range(len(nums)):
    if nums[i]!=sort_arr[i]:
        pos=nums.index(sort_arr[i])
        nums[pos],nums[i]=nums[i],nums[pos]
        cnt+=1
print(cnt)
