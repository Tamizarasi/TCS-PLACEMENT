n=int(input())
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 :
            print('* ',end=' ')
        elif j>n//2 or i==0:
            print('* ',end=' ')
        elif j<n//2 and i==n-1:
            print('* ',end=' ')
        elif i>n//2 and j==n-1:
            print('* ',end=' ')
        elif i<n//2 or j==0:
            print('* ',end=' ')
        else:
            print(' ',end=' ')
    print()
