
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    lock1=x1
    lock2=x2
    k1jump=0
    k2jump=0
    if (x2>x1 or x2==x1) and (v2>v1 or v2==v1):
        return 'NO'
    else:
        while lock1<lock2:
            k1jump+=1
            lock1+=v1
            k2jump+=1
            lock2+=v2
            if lock1==lock2:
                return 'YES'
        return 'NO'        

x1V1X2V2 = input().split(' ')

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(result)