ip1=int(input())
ip2=int(input())
for i in range(ip1,ip2+1):
    if i%2==0:
        continue
    else:
        print(i,end=" ")
