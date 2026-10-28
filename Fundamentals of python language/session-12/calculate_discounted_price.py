# task - 1: Discounted Price Function (get_discounted_price())

def get_discounted_price(price: float, discount_percent: float) -> float:
    """
    Calculates and returns the final price after applying a percentage discount.
    Formula: final_price = price - (price * (discount_percent / 100))
    """
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return round(final_price, 2)


print("=" * 50)
print("            DISCOUNT PRICE CALCULATOR             ")
print("=" * 50)

# Testing with required test values: price = 500, discount = 10%
test_price = 500
test_discount = 10
result = get_discounted_price(test_price, test_discount)

print(f"Original Price   : ₹{test_price}")
print(f"Discount Percent : {test_discount}%")
print(f"Final Price      : ₹{result}")

print("-" * 50)
# Additional test case
custom_price = 1299.0
custom_discount = 15.0
print(f"Test 2: Price ₹{custom_price} with {custom_discount}% off -> ₹{get_discounted_price(custom_price, custom_discount)}")
print("=" * 50)
