# task - 3: Zomato-Style Bill Calculator (float and int Typecasting)

print("=" * 45)
print("             ZOMATO BILL CALCULATOR            ")
print("=" * 45)

# Prompting user for item price and quantity
item_name = input("Enter food item name (optional, e.g., Paneer Tikka): ").strip()
price_input = input("Enter price of the food item: ₹")
quantity_input = input("Enter quantity: ")

# Typecasting inputs: price to float and quantity to int
price = float(price_input)
quantity = int(quantity_input)

# Calculating total bill
total_bill = price * quantity

print("-" * 45)
if item_name:
    print(f"Item Ordered   : {item_name}")
print(f"Item Price     : ₹{price:.2f}")
print(f"Quantity       : {quantity}")
print("-" * 45)

# Displaying required formatted output
print(f"Your total bill is ₹{total_bill:.2f}")
print("=" * 45)
