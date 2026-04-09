def even_numbers(a):
    result = []
    for i in a:
        if i % 2 == 0:
            result.append(i)
    return result

# input
a = [1, 2, 3, 4]

print(even_numbers(a))
