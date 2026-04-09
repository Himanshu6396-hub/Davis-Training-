def total_bill(a):
    s = 0
    for i in a:
        s += i
    return s

# input
a = [100, 200, 300]

print("Total =", total_bill(a))
