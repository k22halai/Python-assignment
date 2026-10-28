# task - 5: Swiggy Total Bill Calculation (reduce() & lambda)

"""
The reduce() function from functools applies a two-argument function 
cumulatively to the items of an iterable, reducing the sequence to a single value.
"""

from functools import reduce

# Given list of item prices for a Swiggy order
item_prices = [120, 80, 150, 60]

print("=" * 60)
print("       SWIGGY BILL ACCUMULATOR (reduce() + lambda)        ")
print("=" * 60)

print(f"Item Prices: {item_prices}\n")

# Using reduce() with a lambda function to accumulate the total bill
# Step-by-step reduction:
# Step 1: 120 + 80  = 200
# Step 2: 200 + 150 = 350
# Step 3: 350 + 60  = 410
total_bill = reduce(lambda accumulator, price: accumulator + price, item_prices)

print(f"Total Bill Amount: ₹{total_bill}")

print("\nReduction Walkthrough:")
print("  (120 + 80) -> 200")
print("  (200 + 150) -> 350")
print("  (350 + 60) -> 410")
print("=" * 60)
