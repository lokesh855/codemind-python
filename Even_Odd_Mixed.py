a=input()
ls=[]
for i in a:
    if int(i)%2==0:
        ls.append("e")
    else:
        ls.append("o")
if 'o' in ls and 'e' in ls:
    print('Mixed')
elif 'o' in ls:
    print('Odd')
else:
    print('Even')
        