start=int(input())
stop=int(input())
for i in range(start,stop+1):
    table=2
    flag=True
    while table*table<=i:
        if i%table==0:
            flag=False
            break
        table+=1
    if flag and i>1:
        print(i,end=" ")
