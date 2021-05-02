
def get_change(m,coins):
    A=[300]*(m+1)
    A[0:6]=(0,1,2,1,1,2)
    if m >= 6:
        for i in range (6, m+1):
            A[i]= min (A[i-coins[0]]+1,A[i-coins[1]]+1,A[i-coins[2]]+1)
        return A[m]
    else:
        return A[m]

if __name__ == '__main__':
    m = int(input())
    coins= [1,3,4]
    print(get_change(m,coins))
