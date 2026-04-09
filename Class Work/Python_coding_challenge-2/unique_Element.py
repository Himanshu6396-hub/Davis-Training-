# input list
a = [1, 1, 2, 3, 3]

b = []   # new list

for i in a:
    if i not in b:
        b.append(i)

# output
print("Count =", len(b))
