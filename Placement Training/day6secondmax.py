size=int(input())
n=list(map(int,input().split()))
maxi=n[0]
secmax=float('inf')
for i in n:
    if i>maxi:
        secmax=maxi
        maxi=i
    elif maxi!=i and i>secmax:
        secmax=i
print(maxi,secmax)
#first and second max
#first and second min
        
