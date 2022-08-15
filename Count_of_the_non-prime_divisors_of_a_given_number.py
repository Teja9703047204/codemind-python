def prime(a):
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc=fc+1
    if fc==2:
        return True
    else:
        return False
x=int(input())
l=[]
c=0
for i in range(1,x+1):
    if x%i==0:
        l.append(i)
for i in l:
    if prime(i)==False:
        c=c+1
print(c)