def prime(n):
    if n%1==0 or n%n==0:
        return 2
    else:
        return 0
n=int(input())
r=prime(n)
if r==2:
    print('yes')
else:
    print('no')
