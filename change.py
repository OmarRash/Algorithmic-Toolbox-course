def get_change(m):
    v=0
    for i in range(150):
        if m ==0:
            return v
        if (m -10)>=0:
            m = m - 10
            v = v + 1
        elif (m - 5) >= 0:
            m = m - 5
            v = v + 1
        else:
            m = m - 1
            v = v + 1
    return v

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
