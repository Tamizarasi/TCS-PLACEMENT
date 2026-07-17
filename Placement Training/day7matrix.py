row,col=map(int,input().split())
matrix=[]
for i in range(row):
    matrix.append(map(int,input().split()))
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()
