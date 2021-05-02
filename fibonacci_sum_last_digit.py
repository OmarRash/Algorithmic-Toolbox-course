def calc_fib_sum_digit(n):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2,n+3):
        a.append((a[i-1]+a[i-2])%10)
    return a[n+2]-1
if __name__=="__main__":
    n = int(input())
    print(calc_fib_sum_digit(n))
