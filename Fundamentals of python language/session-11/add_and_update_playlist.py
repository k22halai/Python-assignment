# task - 2: Add New Key-Value and Update Existing Key in Dictionary

# Initial playlist dictionary
my_playlist = {
    'Blinding Lights': 3.5,
    'Starboy': 3.8,
    'Shape of You': 4.2
}

print("=" * 50)
print("            ADD & UPDATE PLAYLIST SONGS           ")
print("=" * 50)

print(f"Original Playlist:\n{my_playlist}\n")

# 1. Adding a new song and duration using direct assignment
my_playlist['Levitating'] = 3.4
print("1. Added new song 'Levitating' (3.4 mins):")
print(f"   {my_playlist}\n")

# 2. Updating duration of an existing song ('Shape of You' to 4.0 mins)
my_playlist['Shape of You'] = 4.0
print("2. Updated duration of 'Shape of You' to 4.0 mins:")
print(f"   {my_playlist}")

print("=" * 50)
