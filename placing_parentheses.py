# Uses python3
def evalt(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    else:
        assert False
def Max_Min(Max,Min,operations,i,j):
    Max_no = -1000000
    Min_no = 1000000
    for k in range(i , j):
        a=evalt(Max[i][k],Max[k+1][j],operations[k-1])
        b=evalt(Max[i][k],Min[k+1][j],operations[k-1])
        c=evalt(Min[i][k],Max[k+1][j],operations[k-1])
        d=evalt(Min[i][k],Min[k+1][j],operations[k-1])
        Max_no=max(Max_no,a,b,c,d)
        Min_no=min(Min_no,a,b,c,d)
    return (Max_no, Min_no)
def get_maximum_value(dataset):

    length=len(dataset)
    length_integars=int(length/2)+1

    Max=[[0 for x in range(int(length/2)+2)] for x in range(int(length/2)+2)]
    Min=[[0 for x in range(int(length/2)+2)] for x in range(int(length/2)+2)]
    operations=[0 for x in range(int(length/2))]

    for i in range (0,int(length/2)):
        operations[i] = dataset[2*i+1]

    for i in range (1, int(length/2)+2):
        Max[i][i]=int(dataset[2*i-2])
        Min[i][i]=int(dataset[2*i-2])


    for s in range (1,length_integars+1):
        for i in range (1, length_integars-s+1):
            x = i + s
            Max[i][x],Min[i][x]=Max_Min(Max, Min, operations, i ,x)
    return Max[1][int(length/2)+1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
