a,b,c,d=map(int,input().split())
x=(b*c)+abs(a-b)*d
y=(b*c)+abs(a-b)*c
if x<y:
    print(x)
else:
    print(y)