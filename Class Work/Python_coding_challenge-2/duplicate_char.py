# input string
text = input("Enter a string: ")

# store duplicates
dup = ""

for ch in text:
    if text.count(ch) > 1 and ch not in dup:
        dup += ch + " "

# output
print("Duplicates =", dup.strip())
