# input list
a = [10, 20, 5, 15]

# first largest
max1 = a[0]
for i in a:
    if i > max1:
        max1 = i

# second largest
max2 = a[0]
for i in a:
    if i > max2 and i != max1:
        max2 = i

# output
print("Second Largest =", max2)
