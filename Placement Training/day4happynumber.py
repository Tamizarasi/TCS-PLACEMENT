n=int(input())
def happynumber(n):
    total=0
    while n>0:
        total+=((n%10)*(n%10))
        n//=10
    return total
while n!=1 and n!=4:
    n=happynumber(n)
if n==1:
    print('yes')
else:
    print('no')

    
