n=int(input())
x=n**2
def sumofdigits(x):
        if x<10:
            return x
        else:
            return (x%10)+sumofdigits(x//10)
res=sumofdigits(x)
print(res)
if res==n:
    print('Yes')
else:
    print('No')
