n=int(input())
m=list(map(int,input().split()))
for i in range(m):
    for j in range(m[i+1]):
        if m[i]>m[j]:
            print(m[i])
