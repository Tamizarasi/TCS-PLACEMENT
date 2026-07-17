n=int(input())
temp=n
sum1=0
while temp>0:
    sum1+=temp%10
    temp//=10
if sum1%2!=0:
    print('NOT')
else:
    output=sum1//2
    temp=n
    flag=False
    while temp>0:
        digit=temp%10
        if digit == output:
            flag=True
            break
        temp//=10
    if flag:
        print('COOL')
    else:
        print('NOT')
