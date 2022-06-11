n=int(input())
d=n
a=[]
b=str(n)
b=b[::-1]
b=int(b)
n=b
c=0
while n>0:
    r=n%10
    a.append(r)
    n=n//10
for i in range(len(a)):
    c=c+a[i]**(i+1)
if d==c:
    print("True")
else:
    print("False")