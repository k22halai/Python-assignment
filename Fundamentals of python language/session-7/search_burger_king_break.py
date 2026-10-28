# task - 2: Terminate Search Using 'break' Statement

food_items = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King']

print("=" * 50)
print("             SEARCHING FOR BURGER KING            ")
print("=" * 50)

# Iterating through the food items list
for item in food_items:
    if item == 'Burger King':
        print(f"Found {item}, stopping search.")
        break  # Immediately exits the loop
    
    print(f"Checking item: {item}")

print("=" * 50)
