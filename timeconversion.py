#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    l=s.split(':')
    if s.find('AM')>0:
        # it's AM
        if int(l[0])==12:
            return '00:'+l[1]+':'+l[2].replace('AM','')
        return s.replace('AM','')    
    else:
        #it's PM
        t=int(l[0])+12
        if t==24:
            t=12
        return str(t)+':'+l[1]+':'+l[2].replace('PM','')    



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
