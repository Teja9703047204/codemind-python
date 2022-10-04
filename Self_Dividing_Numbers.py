def sdiv(n):
    for i in str(n):
        if i=='0' or n%int(i)>0:
            return False
    return True
n=int(input())
m=int(input())
for i in range(n,m+1):
    if sdiv(i)==True:
        print(i,end=" ")