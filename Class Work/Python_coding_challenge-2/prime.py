def is_prime(n):
    if n < 2:
        return "Not Prime"
    
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

# input
n = int(input("Enter number: "))

print(is_prime(n))
