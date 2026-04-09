# input list
numbers = [5, 8,9,11,6, 2]

# assume first element is maximum
max = numbers[0]

# find maximum 
for num in numbers:
    if num > max:
        max = num

# output
print("Maximum =", max)
