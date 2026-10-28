# task - 4: Slicing Middle Elements from Tuple

fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

print("=" * 50)
print("             TUPLE SLICING (MIDDLE 3 APPS)        ")
print("=" * 50)

print(f"Full Tuple: {fav_apps}\n")

# In a 5-item tuple (indexes 0 to 4):
# Index 0: 'Instagram' (first)
# Indexes 1, 2, 3: 'Zomato', 'Spotify', 'WhatsApp' (middle three)
# Index 4: 'Flipkart' (last)

# Slicing syntax: tuple[start:end] (end index is non-inclusive)
middle_three_apps = fav_apps[1:4]

print(f"Slicing Range      : fav_apps[1:4]")
print(f"Middle Three Apps  : {middle_three_apps}")
print(f"Result Data Type   : {type(middle_three_apps)}")

print("=" * 50)
