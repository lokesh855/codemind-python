import math
n=int(input())
ls=[]
for i in range(n):
    l=int(input())
    ls.append(l)
for i in range(n):
    d=math.sqrt(ls[i])
    if ls[i]==1 or ls[i]==0:
        print("False")
    elif d==int(d):
        print("True")
    else:
        print("False")