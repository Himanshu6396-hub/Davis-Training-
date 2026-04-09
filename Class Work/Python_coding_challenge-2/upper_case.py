# input string
text = input("Enter a string: ")

result = ""

for ch in text:
    # check if character is lowercase
    if 'a' <= ch <= 'z':
        # convert using ASCII
        result += chr(ord(ch) - 32)
    else:
        result += ch

# output
print("Result =", result)
