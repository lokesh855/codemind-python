n=int(input())
ls=[]
for i in range(2):
    l=list(map(int,input().split()))
    ls.append(l)
for i in range(n):
    print(ls[0][i]+ls[1][i],end=' ')
    