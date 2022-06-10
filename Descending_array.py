n=int(input())
l=list(map(int,input().split()))
a=l[:]
a.sort(reverse=True)
if l==a:
    print ("yes")
else:
    print("no")