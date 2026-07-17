row,col=map(int,input().split())
matrix=[]
for i in range(row):
    matrix.append(map(int,input().split()))
maxi=0
for i in matrix:
    for j in i:
        if j>maxi:
            maxi=j
    print(maxi,end=' ')
    print()

