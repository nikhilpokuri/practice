# BUBBLE SORT
def bsort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if(list[i]>list[i+1]):
                list[i],list[i+1]=list[i+1],list[i]
list=[5,9,2,1,67,34,88,34]
print("ORIGINAL LIST:",list)
bsort(list)
print("SORTED LIST:",list)