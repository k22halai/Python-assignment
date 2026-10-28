# task - 1: Flipkart Product Details (Variables & Data Types)

# Variable Declarations
product_name = "Apple iPhone 15 (Black, 128 GB)"  # String (str)
price = 65999.00                                   # Floating-point number (float)
is_available = True                               # Boolean (bool)
rating = 4.6                                      # Floating-point number (float)

print("=" * 50)
print("             FLIPKART PRODUCT DETAILS             ")
print("=" * 50)

# Printing variables and their data types using type() function
print(f"Product Name : {product_name}")
print(f"Data Type    : {type(product_name)}\n")

print(f"Price        : ₹{price}")
print(f"Data Type    : {type(price)}\n")

print(f"Availability : {is_available}")
print(f"Data Type    : {type(is_available)}\n")

print(f"Rating       : {rating} / 5.0")
print(f"Data Type    : {type(rating)}")

print("=" * 50)
