n=input()
a=list(n)
c=0
for i in a:
    if a.count(i)!=1:
        c=1
if(c==0):
    print("True")
else:
    print("False")