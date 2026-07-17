row,col=map(int,input().split())
mat=[]
for i in range(row):
    for j in range(col):
        if i==j:
            mat[i][j]=1
        else:
            mat[i][j]=0
for i in mat:
    for j in i:
        print(j,end=' ')
    print()
