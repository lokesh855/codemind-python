n=input()
a=0
b=0
for i in n:
    if i=='z':
        a+=1
    else:
        b+=1
if a*2==b:
    print("Yes")
else:
    print("No")