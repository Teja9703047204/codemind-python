n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(a,b+1):
    if i in l:
        l.remove(i)
if len(l)>0:
    print(*l)
else:
    print(-1)