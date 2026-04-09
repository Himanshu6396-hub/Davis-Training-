# input strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# remove spaces and convert to lowercase
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# check anagram
if sorted(s1) == sorted(s2):
    print("True")
else:
    print("False")
