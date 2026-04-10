
# opening file in write mode
filev = open("first.txt", "w")

sentences = []

print("Write any five sentences")
for i in range(5):
    sentence = input()
    sentences.append(sentence + "\n")   # newline add kiya
    print("___________")

# writing multiple sentences
filev.writelines(sentences)
print("Data successfully written")

filev.close()

# reading file
file = open("first.txt", "r")
a = file.read()
print(a)
file.close()
