def calc_fib_huge(n,m):
    a = []
    b = []
    a.append(0)
    a.append(1)
    b.append(0)
    b.append(1)
    if n >m :
        n,m=m,n
    for i in range(2, n + 3):
        a.append(a[i - 1]+a[i - 2])

    for i in range(2, m + 3):
        b.append(b[i - 1] + b[i - 2])
    if n==m :
        return a[n] % 10
    return ((b[m+2]-1)-(a[n+1]-1))%10
if __name__=="__main__":
    n ,m =[int(x) for x in input().split()]
    print(calc_fib_huge(n,m))