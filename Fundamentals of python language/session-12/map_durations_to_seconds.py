# task - 3: Convert Song Durations to Seconds (map() & lambda)

"""
The map() function applies a given function (here a lambda) 
to every item in an iterable and returns an iterator.
"""

# Given list of song durations in minutes
song_durations_minutes = [3.5, 4.0, 2.75, 5.2, 1.8]

print("=" * 60)
print("       SONG DURATIONS: MINUTES TO SECONDS (map() + lambda)  ")
print("=" * 60)

print(f"Original Durations (minutes): {song_durations_minutes}\n")

# Using lambda function with map() to convert minutes to seconds (1 minute = 60 seconds)
# Formula: minutes * 60
durations_seconds_map = map(lambda minutes: int(minutes * 60), song_durations_minutes)

# Converting the map object to a list
durations_seconds = list(durations_seconds_map)

print(f"Converted Durations (seconds): {durations_seconds}\n")

# Displaying pair-by-pair conversion for clarity
print("Detailed breakdown:")
for mins, secs in zip(song_durations_minutes, durations_seconds):
    print(f"  {mins} mins -> {secs} seconds")

print("=" * 60)
