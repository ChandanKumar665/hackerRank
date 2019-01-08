import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    # print(a,b)
    i=0
    alice=0
    bob=0
    for x in a:
        if x>(b[i]) and (x)!=(b[i]):
            alice+=1
        elif b[i]>x and b[i]!=x:
            bob+=1
        i+=1  
    return [alice,bob]            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
