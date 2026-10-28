# task - 4: Remove and Pop Apps (remove() and pop() methods)

# Current list of apps
my_fav_apps = ['Instagram', 'WhatsApp', 'Zomato', 'Spotify', 'YouTube', 'LinkedIn', 'ChatGPT']

print("=" * 55)
print("             REMOVE AND POP OPERATIONS            ")
print("=" * 55)

print(f"Starting list:\n{my_fav_apps}\n")

# 1. Removing an app by value using remove()
app_to_remove = 'Zomato'
my_fav_apps.remove(app_to_remove)
print(f"1. Removed '{app_to_remove}' using remove():")
print(f"   Updated List: {my_fav_apps}\n")

# 2. Removing the last app using pop()
popped_app = my_fav_apps.pop()
print(f"2. Popped last app '{popped_app}' using pop():")
print(f"   Updated List: {my_fav_apps}")

print("=" * 55)
