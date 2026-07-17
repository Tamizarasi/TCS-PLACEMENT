n = int(input())
n=n+1
while True:
    temp = n
    rev = 0
    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp //= 10
    if rev == n:
        print(n)
        break
    n += 1
