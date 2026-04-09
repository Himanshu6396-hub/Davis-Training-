# input list
a = [3,7,4,1, 2]

# sorting 
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            # swap
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

# output
print("Sorted =", a)
