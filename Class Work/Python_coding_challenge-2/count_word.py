# input sentence
text = input("Enter a sentence: ")

count = 0

# count spaces
for ch in text:
    if ch == " ":
        count += 1

# words = spaces + 1
print("Words =", count + 1)
