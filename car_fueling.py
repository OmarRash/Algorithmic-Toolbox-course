def compute_min_refills(tank, stops):
    v=0
    cr=0
    z= len(stops) -1
    while cr < z:
        lc=cr
        while cr < z and (stops[cr+1]-stops[lc])<= tank:
            cr = cr + 1
        if cr == lc:
            return -1
        elif cr < z:
            v=v+1
    return v
if __name__ == '__main__':
    d=int(input())
    fd=int(input())
    n=int(input())
    b=[0]
    a=[int(x) for x in input().split()]
    b.extend(a)
    if len(a)==n:
        b.append(d)
        print(compute_min_refills(fd, b))
    else:
        print(-1)
