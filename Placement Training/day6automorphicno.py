n=int(input())
def digitcount(n):
    if n<10:
        return 1
    return 1+digitcount(n//10)
if ((n*n)%(10**digitcount(n))==n):
   print('Yes')
else:
    print('No')
