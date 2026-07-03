https://anotepad.com/notes/62qb4g8x
n=int(input('input='))
for i in range(n,-1,-1):
    print('*'*i)
print()
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()
print()
for i in range(0,n+1):
    for j in range(n,i,-1):
        print(j,end=' ')
    print()
print()
for i in range(1,n+1):
    print(' '*(n-i),'*'*i)
print()
for i in range(n,0,-1):
    print(' '*(n-i),'*'*i)
print()
for i in range(1,n+1):
    print(' '*(n-i),'*'*i)
for i in range(n-1,0,-1):
    print(' '*(n-i),'*'*i)