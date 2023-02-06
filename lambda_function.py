#EVEN NUMBERS USING LAMBDA AND FILTER
print("Enter values to filter even numbers")
arr=[int(input()) for i in range(5)]
print(list(filter(lambda x:x%2==0,arr)))

#CUBE USING LAMBDA
cube=lambda x:x*x*x
print(cube(int(input("Enter a value to get cube:"))))

#first n cube roots
n=int(input("Enter n value to get cubes upto that value :"))
print(list(map(lambda x:x*x*x,[i for i in range(1,n+1)])))

#filtering positive integers
print("Enter values to filter positive integers")
print(list(filter(lambda x:x>0, [int(input()) for i in range(5)])))

#smallest missing positive integer
print("Smallest missing positive integers")
arr=[int(input()) for i in range(5)]
arr=set(arr)
arr=list(filter(lambda x:x>0,arr))
arr.sort()
element=1
for i in arr:
    if i==element:
        element+=1
    else:
        break
print("Smallest missing element is:",element)
