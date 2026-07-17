n=int(input())
temp,count,result=n,0,0
while temp>0:
    count+=1
    temp//=10
temp=n
print(count)
while temp>0:
    result+=((temp%10)**count)
    temp//=10
if result==n:
    print('yes')
else:
    print('no')
    
    
    
    
