# task - 5: Tuple Concatenation (+ operator)

# Existing tuple of 5 favorite apps
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

# Creating another tuple with two new apps to try
new_apps = ('YouTube', 'Blinkit')

print("=" * 55)
print("             TUPLE CONCATENATION (+ OPERATOR)     ")
print("=" * 55)

print(f"fav_apps (5 items) : {fav_apps}")
print(f"new_apps (2 items) : {new_apps}\n")

# Concatenating both tuples into a single tuple called all_apps
all_apps = fav_apps + new_apps

print("-" * 55)
print(f"Combined all_apps  : {all_apps}")
print(f"Total Elements     : {len(all_apps)}")
print(f"Data Type          : {type(all_apps)}")
print("=" * 55)

'''
Note: Concatenation does NOT mutate fav_apps or new_apps. 
Instead, the '+' operator produces a brand-new tuple instance 
containing all combined elements in memory.
'''
