n=int(input())
s=n-1
if (n<=2):
    print("The pattern is not possible")
else:
    for i in range(s,-(s+1),-1):
        for j in range(s,abs(i)-1,-1):
            print("*",end="")
        print()