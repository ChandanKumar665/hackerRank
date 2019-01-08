def diagonalDifference(arr):
    i=0
    j=0
    k=-1
    d1=0
    d2=0
    while i<len(arr):   
        d1+=arr[i][j]
        d2+=arr[i][k]
        i+=1
        j+=1
        k+=-1
    return abs(d1-d2)    