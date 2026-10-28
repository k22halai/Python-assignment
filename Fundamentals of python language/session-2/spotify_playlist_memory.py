# task - 3: Spotify Playlist Details & Memory Addresses (id() function)

"""
The id() function in Python returns the unique identity of an object.
In CPython (standard Python implementation), this integer corresponds 
to the memory address where the object is allocated in RAM.
"""

# Variable Declarations
playlist_title = "Chill Lofi Study Beats"
number_of_songs = 78
is_public = True

print("=" * 65)
print("             SPOTIFY PLAYLIST & MEMORY ADDRESSES                 ")
print("=" * 65)

print(f"Playlist Title : {playlist_title}")
print(f"Memory Address : {id(playlist_title)} (Hex: {hex(id(playlist_title))})\n")

print(f"Number of Songs: {number_of_songs}")
print(f"Memory Address : {id(number_of_songs)} (Hex: {hex(id(number_of_songs))})\n")

print(f"Is Public      : {is_public}")
print(f"Memory Address : {id(is_public)} (Hex: {hex(id(is_public))})")

print("=" * 65)
