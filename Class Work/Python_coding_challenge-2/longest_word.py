# input string
text = input("Enter a sentence: ")

# split into words
words = text.split()

# assume first word is longest
longest = words[0]

# find longest word
for word in words:
    if len(word) > len(longest):
        longest = word

# output
print("Longest word =", longest)
