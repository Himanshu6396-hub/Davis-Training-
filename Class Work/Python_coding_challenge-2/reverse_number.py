# input to reverse number 
a=int(input("Enter number"))
b=0
#To reverse number 
while a>0:
  c=a%10
  b=b*10+c
  a=a//10
print("Reverse number is:",b)
