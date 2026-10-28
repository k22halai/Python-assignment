# task - 4: Filter Products Starting with 'M' (filter() & lambda)

"""
The filter() function constructs an iterator from elements of an iterable 
for which a function (here a lambda) returns True.
"""

# Example Flipkart-style product catalog
product_list = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

print("=" * 60)
print("     FILTER PRODUCTS STARTING WITH 'M' (filter() + lambda)   ")
print("=" * 60)

print(f"Original Product Catalog:\n{product_list}\n")

# Using filter() with a lambda function checking if product starts with 'M'
m_products_filter = filter(lambda product: product.startswith('M'), product_list)

# Converting the filter object to a list
m_products = list(m_products_filter)

print("Filtered Products (starting with 'M'):")
print(m_products)
print(f"\nTotal Matching Products: {len(m_products)}")

print("=" * 60)
