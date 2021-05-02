import math
def merge_sort(a, b):
    indexa =0
    indexb =0
    c=[]
    while indexa < len(a) and indexb < len(b):
        if a[indexa]> b[indexb]:
            c.append(a[indexa])
            indexa = indexa+1
        else:
            c.append(b[indexb])
            indexb=indexb+1
    if indexa==len(a):c.extend(b[indexb:])
    else: c.extend(a[indexa:])
    return c
def merge(a):
    if len(a) == 1 :
        return a
    x=int((len(a)/2))
    left =merge(a[: x])
    right=merge(a[x :])
    return merge_sort(left, right)

def get_majority_element (A, right):
    c=[0]*right
    c=merge(A)
    count=0
    for i in range(1,right):
        if c[i] == c[i-1]:
            count += 1
            if count==math.floor((right/2)):
                return 1
        else: 
            count = 0
    return 0
        

if __name__ == '__main__':
    elements = input()
    data = [int(x) for x in input().split()]
    print (get_majority_element (data, int(elements)))

