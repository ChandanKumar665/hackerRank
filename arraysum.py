import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    res=0
    for x in ar:
        res+=x
    return res    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
