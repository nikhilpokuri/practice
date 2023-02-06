arr1 = [1,2,3,4,5,6,7,8]
arr2 = [7,8,9,10,11]
arr3 = [7,8,21,0]

#method 1
print(sorted(set(arr1) & set(arr2) & set(arr3)))

#method 2
arr1 = set(arr1)
arr2 = set(arr2)
arr3 = set(arr3)
temp = arr1.intersection(arr2)
print(sorted(arr3.intersection(temp)))
