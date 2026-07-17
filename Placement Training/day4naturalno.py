def naturalno(n):
    if n==0:
        return 0
    else:
        return n+naturalno(n-1)
n=int(input())
print(naturalno(n))
