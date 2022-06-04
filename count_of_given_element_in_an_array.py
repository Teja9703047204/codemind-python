n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=0
for i in l:
    if i==a:
        c=c+1
print(c)