n=list(map(int,input().split()))
print(*n[2:],*n[:2])
    

n=list(map(int,input().split()))
#12345 - 45123
for i in range(len(n)-2):
   m=n[-2]
    p=n[-1]
    a.append(n[i])
print(m,p,*a)    
