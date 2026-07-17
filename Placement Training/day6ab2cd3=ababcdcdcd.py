n=input()
s=''
for i in n:
    if i>='a' and i<='z':
        s+=i
    else:
        count=ord(i)-48
        print(s*count,end='')
        s=''
i=0
while i<len(n):
    while i<len(n) and n[i]>='a' and n[i]<='z':
        s+=n[i]
        i+=1
    digit=1
    count=0
    while i<len(n) and n[i]>='0' and n[i]<='9':
        count=ord
