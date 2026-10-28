# task - 2: Zomato Restaurant Details (Naming Rules & Declaration)

"""
Python Variable Naming Rules followed:
1. Meaningful & descriptive names in lowercase with words separated by underscores (snake_case) per PEP 8.
2. Must begin with a letter (a-z, A-Z) or an underscore (_).
3. Cannot begin with a number.
4. Can only contain alphanumeric characters and underscores (a-z, A-Z, 0-9, and _).
5. Variable names are case-sensitive (e.g., average_cost != Average_Cost).
6. Cannot use reserved Python keywords (e.g., class, def, return, for).
"""

# Variable Declarations complying with Python naming rules
restaurant_name = "Barbeque Nation"
cuisine_type = "North Indian, BBQ, Continental"
average_cost = 1400.00
is_open_now = True

print("=" * 55)
print("             ZOMATO RESTAURANT INFORMATION             ")
print("=" * 55)

print(f"Restaurant Name : {restaurant_name}")
print(f"Cuisine Type    : {cuisine_type}")
print(f"Average Cost    : ₹{average_cost} for two")
print(f"Currently Open  : {is_open_now}")

print("=" * 55)
