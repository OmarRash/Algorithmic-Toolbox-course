def knapsack_Gold(TW, NW, A):

    array = [[0 for x in range(TW+ 1)] for x in range(NW + 1)]

    for i in range(1, NW + 1):
        for j in range(1, TW + 1):
            array[i][j] = array[i-1][j]
            if A[i-1] <= j:
                value = array[i-1][j - A[i-1]] + A[i-1]
                if value > array[i][j]:
                    array[i][j] = value

    return array[NW][TW]
 
if __name__=='__main__':

    constranis = [int(x) for x in input().split()]
    TW = constranis[0]
    no_of_weights = constranis[1]
    weights = [int(x) for x in input().split()]
    print(knapsack_Gold(TW, no_of_weights, weights))