def calc_pisano(n,m):
    a = []
    a.append(0)
    a.append(1)
    y = 0
    for i in range(2,pow(10,14)):
        a.append((a[i-1]+a[i-2]) % m)
        if a[i-1]==0 and a[i]==1:
            x =len(a)-2
            y = n % x
            return y
    return 0
def calc_fib(n,m):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2 , n+1):
        a.append((a[i-1]+a[i-2])%m)
    return a[n]
if __name__=="__main__":
    n ,m =[int(x) for x in input().split()]
    y =calc_pisano(n ,m )
    print(calc_fib(y, m))
