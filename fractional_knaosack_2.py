def get_optimal_value(capacity, weights, c):
    v = 0
    z=len(c)
    for i in range(z):
        x=max(c)
        for j in range (z):
            if x==c[j] :
                y = j
                break
        if capacity==0:
            return v
        if weights[y]>0:
            a = min( weights[y] , capacity )
            v = v + a * (c[y])
            capacity = capacity - a
            c[y]=0
            weights[y]=0
    return v
if __name__ == "__main__":
    n, capacity = [int(x) for x in input().split()]
    weights = []
    values = []
    c = []
    for i in range (n):
        value, weight = [int(x) for x in input().split()]
        values.append(value)
        weights.append(weight)
        c.append(value/weight)
    formatted_float = "{:.4f}".format(get_optimal_value(capacity,weights,c))
    print(formatted_float)