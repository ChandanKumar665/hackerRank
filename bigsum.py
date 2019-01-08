import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    i=1
    n=len(ar)
    k=(n/2)
    k=int(k)
    j=0
    sum_res=0
    while j<=(k):
        if (k+i)<n:
            sum_res+=(ar[j]+ar[k+i])
        else:
            sum_res+=ar[j]    
        i+=1
        j+=1
    return sum_res    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
