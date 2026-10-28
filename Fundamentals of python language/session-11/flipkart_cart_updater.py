# task - 5: Flipkart Cart Updater Function (update_cart())

def update_cart(cart: dict, item: str, qty: int) -> dict:
    """
    Adds a new item to a Flipkart-style cart dictionary or updates 
    the quantity if the item already exists, then returns the updated cart.
    Uses dictionary update() or direct assignment.
    """
    # Updating or adding the item using direct key assignment (or cart.update({item: qty}))
    cart[item] = qty
    return cart


# Demonstration
print("=" * 60)
print("             FLIPKART CART MANAGEMENT SYSTEM              ")
print("=" * 60)

# Initial shopping cart
flipkart_cart = {
    'Wireless Earbuds': 1,
    'Fast Charger': 2
}

print(f"Initial Cart:\n{flipkart_cart}\n")

# 1. Adding a new item to the cart
print("1. Adding new item 'Smartphone Case' with qty 1:")
update_cart(flipkart_cart, 'Smartphone Case', 1)
print(f"   Current Cart: {flipkart_cart}\n")

# 2. Updating quantity of an existing item in the cart
print("2. Updating quantity of 'Wireless Earbuds' from 1 to 3:")
update_cart(flipkart_cart, 'Wireless Earbuds', 3)
print(f"   Current Cart: {flipkart_cart}\n")

# 3. Adding another item using update() syntax demonstration
print("3. Adding 'Smart Watch' with qty 1:")
update_cart(flipkart_cart, 'Smart Watch', 1)
print(f"   Final Cart  : {flipkart_cart}")

print("=" * 60)
