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
def rev(n):
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
m=rev(n)
if(prime(n)==True and prime(m)==True):
    print("circular prime")
elif(prime(n)==True and prime(m)==False):
    print("prime but not a circular prime")
else:
    print("not prime")