a=int(input())
b=a*a
c=0
for i in str(b):
    c=c+int(i)
if c==a:
    print('Neon Number')
else:
    print('Not Neon Number')
    