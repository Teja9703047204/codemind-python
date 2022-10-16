n=int(input())
l=list(map(int,input().split()))
c=0
m=0
for i in range(n):
    c=0
    for j in range(i,n,1):
        if(l[j]==1):
            c=c+1
        else:
            break
    if(c>m):
        m=c
print(m)