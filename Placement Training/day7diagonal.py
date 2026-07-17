row,col=map(int,input().split())
mat=[]
for i in range(row):
    mat.append(list(map(int,input().split())))
for i in range(row):
    for j in range(col):
        if i==j:
            print(mat[i][j],end=' ')
    print()
