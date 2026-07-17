n=int(input())
def harshadnumber(n):
    total=0 
    while n>0:
        total+=n%10
        n//=10
    return total
res=harshadnumber(n)
if n%res==0:
    print('yes')
else:
    print('no')
