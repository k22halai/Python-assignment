# task - 4: Dictionary Methods: keys(), values(), and items()

# Given food_order dictionary
food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}

print("=" * 55)
print("             ZOMATO FOOD ORDER DICTIONARY         ")
print("=" * 55)

print(f"Dictionary: {food_order}\n")

# a) All food items using the keys() method
print("a) All Food Items (using .keys()):")
for item in food_order.keys():
    print(f"   - {item}")
print()

# b) All quantities using the values() method
print("b) All Quantities (using .values()):")
for quantity in food_order.values():
    print(f"   - {quantity}")
print()

# c) Each item with its quantity using the items() method
print("c) Item with Quantity (using .items()):")
for item, qty in food_order.items():
    print(f"   - {item}: {qty} ordered")

print("=" * 55)
