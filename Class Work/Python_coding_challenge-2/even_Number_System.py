# To filter even numbers 
#Take input number for limit 
even =[]
num=int(input("Enter the limit to find even numbers "))
for i in range(num):
  if i%2==0:
    even.append(i)
# to print list of even numbers
print(*even)
    
