# input number
a = int(input("Enter number: "))

# store original number
temp = a

# reverse number
b = 0
while a > 0:
    b = b * 10 + (a % 10)
    a = a // 10

# check palindrome
if temp == b:
    print("Palindrome")
else:
    print("Not Palindrome")
