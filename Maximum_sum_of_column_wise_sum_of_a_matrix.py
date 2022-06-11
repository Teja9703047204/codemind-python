def sum(c):
    a=[]
    for i in range(len(c[0])):
        t=0
        for j in c:
            t=t+j[i]
        a.append(t)
    return a
n,m=map(int,input().split())
mat=[]
c=0
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)
print(max(sum(mat)))