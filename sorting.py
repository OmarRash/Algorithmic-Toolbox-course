import random
def partition3(a, l, r):
    m1=int(l)
    m2=int(l) 
    count=0
    x = a[l]
    for i in range(1+l,r+1):
        if a[i] < x:
            m1 += 1
            a[i], a[m1] = a[m1], a[i]
            
        if a[i] == x:
            count += 1
            m1+=1
            a[i], a[m1] = a[m1], a[i]
            a[l+count], a[m1] = a[m1] , a[l+count]
    m2 = m1
    m1= m2-count
    for i in range(m1, m2+1) :
        y = a[i]
        a[i] = a[l+(m2-i)]
        a[l+(m2-i)] = y

        
    return (m1,m2)
def randomized_quick_sort(a, l, r):
    if l >= r:
        return a[l]
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    if m1-1 >= l:
        randomized_quick_sort(a, l, m1 - 1)
    if m2+1 <= r:
        randomized_quick_sort(a, m2 + 1, r)
    return a


if __name__ == '__main__':
    size =int(input())
    data = [int(x) for x in input().split()]
    out=randomized_quick_sort(data, 0, size-1)
    print(*out)

