n=input()
m=input()
a=n.lower()
b=m.lower()
c=0
for i in a:
    if i not in b:
        c=1
if c==0:
    print("True")
else:
    print("False")