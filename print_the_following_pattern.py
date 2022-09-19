n=int(input())
a=n-1
for i in range(n):
    for j in range(n):
        if(i==j or a-i==j):
            print("x",end="")
        else:
            print(0,end="")
    print()