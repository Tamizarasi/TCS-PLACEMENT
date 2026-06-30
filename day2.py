import script1
import script2
n=input()
if n<2:
    print('no')
else:
    prime=True
    i=2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1
    if prime:
        print('yes')
    else:
        print('no')
Integer_to_binary=script1.inttobin(n,s)
print(Integer_to_binary)
print(script2.bintoint(n))

script1

def inttobin(n,s):
    while n>0:
        s=str(n%2)+s
        n//=2
    return s

script2

def bintoint(n):
    res=0
    for i in range(len(n)-1,-1,-1):
        if i==1:
            res+=2**i
        else:
            res+=0
    return res