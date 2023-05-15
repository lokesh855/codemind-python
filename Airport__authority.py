n=int(input())
ls=[]
for i in range(n):
    ls.append(int(input()))
wt=int(input())
final=0
for i in ls:
    if i<=wt:
        final+=1
    else:
        final+=2
print(final)
    