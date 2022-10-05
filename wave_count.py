n=int(input())
lst=list(map(int,input().split()))
c=0
d=0
for i in range(0,n-2,2):
    if (lst[i]<lst[i+1]):
        if (lst[i+1]>lst[i+2]):
            c=c+1
        else:
            d=d+1
    elif lst[i]>lst[i+1]:
        if lst[i+1]<lst[i+2]:
            c=c+1
        else:
            d=d+1
if d==0:
    print(c)
else:
    print(-1)