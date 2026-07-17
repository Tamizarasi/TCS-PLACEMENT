s=input()
word=''
res=''
for i in s:
    if i==' ':
        res+=word+' '
        word=''#word is resets
    else:
        word=i+word
res+=word
print(res)
