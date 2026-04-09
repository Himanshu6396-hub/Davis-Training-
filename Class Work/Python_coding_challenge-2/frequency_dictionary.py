a = [1, 2, 2, 3]

freq = {}

for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency =", freq)
