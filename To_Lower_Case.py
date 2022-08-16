n=input()
a=""
for i in n:
    if i.isupper()==True:
        a+=i.lower()
    else:
        a+=i
print(a)