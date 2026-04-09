# input number
a = int(input("Enter number: "))

# sum of digits
sum = 0
while a > 0:
    digit = a % 10
    sum += digit
    a = a // 10

# output
print("Sum =", sum)
