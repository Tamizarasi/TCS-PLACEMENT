a=[2,3,4,6,8]
even=[]
odd=[]
for i in range(len(a)):
    if a[i]& 1==0:
        even.append(a[i])
    else:
        odd.append(a[i])
print(sum(even),sum(odd))
