s=input()
i=0
while i<len(s):
    char=s[i]
    i+=1
    digit,power=0,1
    while i<len(s)and s[i]>='0' and s[i]<='9':
        digit=ord(s[i])-48+power*digit
        power*=10
        i+=1
    print(char*digit,end='')
        
