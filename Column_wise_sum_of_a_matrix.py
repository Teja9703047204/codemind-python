def sum(n):
    a=[]
    for i in range(len(n[0])):
        t=0
        for j in n:
            t=t+j[i]
        a.append(t)
    return a
m,n=map(int,input().split())
mat=[]
for i in range(m):
    l=list(map(int,input().split()))
    mat.append(l)
print(*(sum(mat)))