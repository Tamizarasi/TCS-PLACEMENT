s=input()
res=1
for i in range(len(s)):
    if s[i]=='A':
        res=res and s[i+1]
    if s[i]=='B':
        res=res or s[i+1]
    if s[i]=='C':
        res=res ^ s[i+1]
print(res)
