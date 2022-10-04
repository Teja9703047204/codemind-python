import math
def prime(n):
    fc=0
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            fc=fc+1
    if(fc==0):
        return True
    else:
        return False;
n=int(input())
m=int(input())
a=n+m
for i in range(1,1000):
    if(prime(a+i)==True):
        print(i)
        break