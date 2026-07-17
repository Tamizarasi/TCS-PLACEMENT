s=input()
count=0
for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        count+=1
    elif i==' ':
        continue
print(count)
if count==26:
    print('Yes')
else:
    print('No')
