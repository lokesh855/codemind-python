n=int(input())
b=0;c=0
for i in range(n+1):
    b=b+(i*i)
for i in range(n+1):
    c=c+i
print((c*c)-b)