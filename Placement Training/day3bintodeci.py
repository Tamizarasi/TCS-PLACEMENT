n=int(input())
deci,bina=0,1
while n>0:
    rem=n%10
    deci=deci+(rem*bina)
    bina*=2
    n=n//10
print(deci)
