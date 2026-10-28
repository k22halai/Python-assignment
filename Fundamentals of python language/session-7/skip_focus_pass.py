# task - 3: Placeholder Control Using 'pass' Statement

"""
The 'pass' statement in Python is a null statement (no-op). 
It serves as a placeholder where syntactically code is required, 
but no action needs to be executed.
"""

playlists = ['Chill Vibes', 'Workout', 'Focus', 'Party']

print("=" * 45)
print("             PLAYLIST INSPECTION              ")
print("=" * 45)

for playlist in playlists:
    # When playlist is 'Focus', execute pass (no action performed)
    if playlist == 'Focus':
        pass  # Placeholder: do nothing for 'Focus'
    else:
        # Prints all other playlist names
        print(playlist)

print("=" * 45)
