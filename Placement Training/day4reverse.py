def rev(t,n):
    if n<10:
        return t*10+n
    else:
        t=t*10+(n%10)
        return rev(t,n//10)
n=int(input())
print(rev(n))
