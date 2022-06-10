n=int(input())
n=str(n)
a=list(n)
c=0
for i in a:
    c=c+1
if c!=10:
    print("Invalid")
elif n.startswith('0')==True:
    print("invalid")
else:
    print("Valid")