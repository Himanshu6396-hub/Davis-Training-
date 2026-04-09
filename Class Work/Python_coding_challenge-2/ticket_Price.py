# Input day
day = input("Enter day: ")

# Convert to lowercase for easy comparison
day = day.lower()

# Determine ticket price
if day == "sunday":
    price = 200
elif day == "monday":
    price = 180
elif day == "saturday":
  price = 170
else:
    price = 150

# Output result
print("Ticket Price =", price)
