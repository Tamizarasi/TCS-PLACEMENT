s1=input().lower()
s2=input().lower()
res=''
for i in s1:
    for j in s2:
        if i==j:
            res+=i
        elif i==' ':
            continue
print(res==s1)
#if sorted(n)==sorted(m):
#True
#else:
#flase
            
    
