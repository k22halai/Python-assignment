# task - 3: Demonstrate Tuple Immutability & TypeError

fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

print("=" * 55)
print("             TUPLE IMMUTABILITY TEST              ")
print("=" * 55)

print(f"Original Tuple: {fav_apps}\n")

# Attempting to modify the first element of the tuple
print("Attempting operation: fav_apps[0] = 'YouTube'")

try:
    fav_apps[0] = 'YouTube'
except TypeError as error:
    print(f"\nCaught Expected Error: {type(error).__name__}")
    print(f"Error Message        : {error}")

print("=" * 55)

'''
================================================================================
EXPLANATION: WHY DOES THIS ERROR OCCUR? (TUPLE IMMUTABILITY)
================================================================================
1. In Python, tuples are IMMUTABLE data structures. Once a tuple is created, 
   its elements cannot be added, removed, replaced, or modified in-place.

2. When we attempt item assignment like `fav_apps[0] = 'YouTube'`, Python 
   raises a `TypeError: 'tuple' object does not support item assignment`.

3. Why Tuples are Immutable:
   - Data Integrity: Protects critical data from being accidentally modified.
   - Memory Optimization: Tuples are allocated in a fixed block of memory, 
     making them faster and lighter in memory compared to mutable lists.
   - Hashability: Because they are immutable, tuples can be used as dictionary 
     keys or stored in sets (as long as all elements are hashable).
================================================================================
'''
