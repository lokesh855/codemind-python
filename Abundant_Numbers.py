a=int(input())
cnt=0
for i in range(1,a):
    if a%i==0:
        cnt=cnt+i
if(cnt>a):
    print("True")
else:
    print("False")
    