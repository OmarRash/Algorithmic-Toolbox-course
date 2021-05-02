def calc_fib(n):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2 , n+1):
        a.append((a[i-1]+a[i-2])%10)
    return a[n] % 10
if __name__=="__main__":
    n = int(input())
    print(calc_fib(n))
