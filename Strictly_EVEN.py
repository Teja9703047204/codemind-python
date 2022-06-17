n=int(input())
l=list(map(int,input().split()))
a=1
for i in range(n):
    if l[i]%2==0:
        if i%2==1:
            print('False')
            break
else:
    print("True")