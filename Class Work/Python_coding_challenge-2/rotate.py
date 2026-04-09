# input list
a = [1, 2, 3]

# store last element
last = a[-1]

# shift elements to right
for i in range(len(a)-1, 0, -1):
    a[i] = a[i-1]

# place last element at first
a[0] = last

# output
print("Result =", a)
