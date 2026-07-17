n=input()
flag=[False]*26
for i in n:
    if i>='a' and i<='z':
        flag[ord(i)-97]=True
    elif i>='A' and i<='Z':
        flag[ord(i)-65]=True
for i in flag:
    if not(i):
        print('Not a panagram')
    else:
        print('Panagram')
