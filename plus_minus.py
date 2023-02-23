def plusMinus(arr):
    pos = list(filter(lambda x:x>0,arr))
    neg = list(filter(lambda x:x<0,arr))
    zer = list(filter(lambda x:x==0,arr))
    
    print(len(pos)/len(arr))
    print(len(neg)/len(arr))
    print(len(zer)/len(arr))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
