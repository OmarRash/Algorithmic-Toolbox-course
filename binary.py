import math

def binarySearch (A,low,high,B_elemnet):
    x=(high-low)/2
    mid=low+math.floor(x)
    if low>high:
        return -1
    elif A[mid] == B_elemnet:
        return mid
    elif A[mid] > B_elemnet:
        return binarySearch (A, low, mid-1, B_elemnet)
    else:
        return binarySearch (A, mid+1, high, B_elemnet)

if __name__ == '__main__':
    a=[int(x) for x in input().split()]
    data=a[1:a[0]+1]

    b=[int(x) for x in input().split()]
    inputarr=b[1:b[0]+1]

    low=0
    high=a[0]-1
    b_length=b[0]
    
    for i in inputarr :
        print(binarySearch(data,low,high,i), end = ' ')



