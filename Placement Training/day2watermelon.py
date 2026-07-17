w=int(input())
if w>99:
    print('invalid')
elif w%2!=0:
    print('No')
else:
    print('Yes')
    half=w//2
   # print(half)
    if half%2==0:
        print(half,' ',half)
    else:
        print(half-1,' ',half+1)
