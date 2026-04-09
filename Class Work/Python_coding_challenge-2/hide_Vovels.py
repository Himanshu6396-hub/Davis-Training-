# input string
text = input("Enter a string: ")

result = ""

# replace vowels
for ch in text:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        result += "*"
    else:
        result += ch

# output
print("Result =", result)
