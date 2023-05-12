import math
a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    cnt=cnt+math.sqrt(i)
print("%0.2f"%cnt)