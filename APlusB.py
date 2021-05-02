def pairwise (a, n):
    index1 = 0
    index2 = 0
    x = 0
    for i in range (n):
        if a[i]>index1 :
            index1 = a[i]
            x = i
    for j in range(n):
        if a[j] > index2 and j != x :
            index2 = a[j]
    return ( index1 * index2 )
if __name__== "__main__" :
    a =[]
    y = int (input())
    a = list(map(int, input().strip().split()))
    print(pairwise(a,y))












