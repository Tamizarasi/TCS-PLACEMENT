n=int(input())
prod=1
while n>0:
    digit=n%10
    prod=prod*digit
    n=n//10
print(prod)
