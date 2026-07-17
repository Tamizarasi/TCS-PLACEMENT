ones =["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
twos = ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
n = int(input()) 
if n < 10:
  print(ones[n])
elif n < 20:
  print(twos[n%10])
elif n < 100:
  print(tens[(n//10)-1]+' '+ones[n%10])
elif n<1000:
  print(ones[(n//10)//10]+' hundred and '+tens[((n//10)%10)-1]+' '+ones[n%10])
     
