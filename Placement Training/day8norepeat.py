a=list(map(int,input().split()))
a.sort()
for i in range(len(a)):
    flag=False
    for j in range(i):
        if a[i]==a[j]:
            flag=True
            break
    if not flag:
        print(a[i],end=' ')
#1122558899
#i=0123456789
