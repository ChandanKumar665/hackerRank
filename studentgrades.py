#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    l=[]
    for x in grades:
        if x < 38:
            l.append(x)
        else:
            next_mul=(int(x/5)+1)*5
            if (next_mul-x)<3:
                l.append(next_mul)
            else:
                l.append(x)
    return l                


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
