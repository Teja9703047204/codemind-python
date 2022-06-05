n=int(input())
l=list(map(int,input().split()))
a=1
for i in l:
    a=a*i
for i in l:
    print(a//i,end=" ")