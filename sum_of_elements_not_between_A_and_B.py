n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(a,b+1):
    if i in l:
        l.remove(i)
print(sum(l))