def hcf(a,b):
    if a>b:
        h=a
        s=b
    else:
        h=b
        s=a
    for i in range(h,0,-1):
        if h%i==0:
            if s%i==0:
                return i
a=int(input())
lst=list(map(int,input().split()))
l=0
for i in lst:
    l=hcf(l,i)
print(l)