n=input()
n=list(n)
for i in n:
    if i!='.':
        print(i,end="")
    elif i=='.':
        print('[.]',end="")