# input string
text = input("Enter a string: ")

# vowel count
count = 0
for ch in text:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        count += 1
# output
print("Vowels =", count)
