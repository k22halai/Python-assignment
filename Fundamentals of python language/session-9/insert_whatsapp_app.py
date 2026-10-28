# task - 3: Insert App at Second Position (insert() method)

# Current list of apps
my_fav_apps = ['Instagram', 'Zomato', 'Spotify', 'YouTube', 'LinkedIn', 'ChatGPT']

print("=" * 55)
print("       INSERT 'WhatsApp' AT SECOND POSITION (INDEX 1)     ")
print("=" * 55)

print(f"List before insert:\n{my_fav_apps}\n")

# Note: Python uses 0-based indexing.
# 1st position -> index 0 ('Instagram')
# 2nd position -> index 1
my_fav_apps.insert(1, 'WhatsApp')

print("Inserted 'WhatsApp' at index 1.")
print(f"Updated my_fav_apps list:\n{my_fav_apps}")
print("=" * 55)
