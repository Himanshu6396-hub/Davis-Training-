# input string
text = input("Enter a string: ")

# reverse string
rev = text[::-1]

# check palindrome
if text == rev:
    print("Yes")
else:
    print("No")
