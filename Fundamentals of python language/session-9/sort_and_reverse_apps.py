# task - 5: Sort and Reverse Apps List (sort() and reverse() methods)

# Current list of apps
my_fav_apps = ['Instagram', 'WhatsApp', 'Spotify', 'YouTube', 'LinkedIn']

print("=" * 60)
print("       SORT & REVERSE APPS (USING ONLY LIST METHODS)       ")
print("=" * 60)

print(f"Original List:\n{my_fav_apps}\n")

# CONSTRAINT: Use ONLY list methods, not built-in sorted().
# 1. Sorting in alphabetical order using list method .sort()
my_fav_apps.sort()
print("1. Alphabetical Order (using my_fav_apps.sort()):")
print(f"   {my_fav_apps}\n")

# 2. Reversing the sorted list using list method .reverse()
my_fav_apps.reverse()
print("2. Reversed Order (using my_fav_apps.reverse()):")
print(f"   {my_fav_apps}")

print("=" * 60)
