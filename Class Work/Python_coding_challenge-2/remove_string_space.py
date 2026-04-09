# input string
text = input("Enter a string: ")

# remove spaces
result = ""
for ch in text:
    if ch != " ":
        result += ch

# output
print("Result =", result)
