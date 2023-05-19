a=input()
cnt=0
b='0123456789'
for i in a:
    if i in b:
        cnt=cnt+int(i)
print(cnt)