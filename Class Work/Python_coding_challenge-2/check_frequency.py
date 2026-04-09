# input string
text = input("Enter a string: ")

# input character
ch = input("Enter character: ")

# count occurrence
count = 0
for c in text:
    if c == ch:
        count += 1

# output
print("Count =", count)
