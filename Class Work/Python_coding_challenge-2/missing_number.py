# input list
a = [1, 2, 4, 5]

# find n (last number)
n = max(a)

# expected sum (1 to n)
total = n * (n + 1) // 2

# actual sum
s = 0
for i in a:
    s += i

# missing number
missing = total - s

# output
print("Missing =", missing)
