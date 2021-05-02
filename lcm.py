def gcd_euc(a,b):
    if b ==0:
        return a
    x=(a % b)
    a, b = b, x
    return  gcd_euc(a,b)
if __name__ == "__main__":
    a, b = [int(x) for x in input().split()]
    x= gcd_euc(a, b)
    print((int(a/x)*b))
