# input dictionary
a = {"A":80, "B":95, "C":78}

# assume first student is highest
max_key = list(a.keys())[0]

for k in a:
    if a[k] > a[max_key]:
        max_key = k

print("Highest =", max_key)
