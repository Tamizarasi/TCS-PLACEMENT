s=input()
count=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' :
        continue
    elif i>='a' and i<='z'  or i>='A' and  i<='Z':
        count+=1
print(count)
