# Name: Atul Thite
# Project: Personal Information Manager

# Welcome Message
print("=" * 50)
print("      PERSONAL INFORMATION MANAGER")
print("=" * 50)

# Static Information
name = "Atul Thite"
age = 21
city = "Kolhapur"
hobby = "Coding"

# Get User Input
favorite_food = input("Enter your favorite food: ").strip()

while favorite_food == "":
    print("Food cannot be empty!")
    favorite_food = input("Enter your favorite food: ").strip()

favorite_color = input("Enter your favorite color: ").strip()

while favorite_color == "":
    print("Color cannot be empty!")
    favorite_color = input("Enter your favorite color: ").strip()

# Calculate Age in Months
age_in_months = age * 12

# Display Information
print("\n" + "=" * 50)
print("           YOUR INFORMATION")
print("=" * 50)

print(f"Name           : {name.title()}")
print(f"Age            : {age} years")
print(f"Age in Months  : {age_in_months} months")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.title()}")
print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.title()}")

# Goodbye Message
print("\n" + "=" * 50)
print("Thank you for using Personal Information Manager!")
print("=" * 50)