n=int(input())
result=0
for i in range(1,n+1):
    result=n%2
    n//=2
    print(result,end=' ')
