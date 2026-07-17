s=input()
word=''
res=''
for i in range(len(s)-1,-1,-1):
    if s[i]==' ':
        res=word+' '
        word=''
    else:
        word=s[i]+word
res+=word
print(res)
