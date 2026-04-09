# input lists
list1 = [1, 4, 3]
list2 = [2, 3, 4]

# find common elements
result = []

for num in list1:
    if num in list2 and num not in result:
        result.append(num)

# output
print("Common =", result)
