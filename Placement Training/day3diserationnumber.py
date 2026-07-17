n=int(input())
temp,count,result=n,0,0
while temp>0:
    count+=1
    temp//=10
temp=n
#print(count)
for i in range(count,0,-1):
    result+=((temp%10)**i)
    temp//=10
print(result)
    
    
    
    
