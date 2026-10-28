# task - 2: Append New App to List (append() method)

# Initial list of favorite apps
my_fav_apps = ['Instagram', 'Zomato', 'Spotify', 'YouTube', 'LinkedIn']

print("=" * 50)
print("            APPEND NEW APP TO LIST            ")
print("=" * 50)

print(f"List before append:\n{my_fav_apps}\n")

# Adding a newly started app using append() (adds to the end of the list)
new_app = 'ChatGPT'
my_fav_apps.append(new_app)

print(f"Added app: '{new_app}'")
print(f"Updated my_fav_apps list:\n{my_fav_apps}")
print("=" * 50)
