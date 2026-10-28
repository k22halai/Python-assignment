# task - 2: Extract Artist from Spotify Song Title (String Slicing & index())

def extract_artist(song_title: str) -> str:
    """
    Extracts and returns the artist's name from a song title formatted as 'Song Name - Artist Name'.
    Uses the index() method to find the position of '-' and slices the string.
    """
    if '-' not in song_title:
        return "Invalid format: Dash '-' not found."
    
    # Finding the position of the dash
    dash_position = song_title.index('-')
    
    # Slicing from the character after the dash to the end of the string
    artist_name = song_title[dash_position + 1:].strip()
    return artist_name


# Test demonstration
print("=" * 55)
print("             SPOTIFY ARTIST EXTRACTOR             ")
print("=" * 55)

sample_songs = [
    "Blinding Lights - The Weeknd",
    "Starboy - Daft Punk",
    "Shape of You - Ed Sheeran",
    "Stay - Justin Bieber"
]

for track in sample_songs:
    artist = extract_artist(track)
    print(f"Track : \"{track}\"")
    print(f"Artist: \"{artist}\"\n")

# Interactive input option
user_song = input("Enter a track (e.g., 'Levitating - Dua Lipa'): ").strip()
if user_song:
    print(f"Extracted Artist: {extract_artist(user_song)}")

print("=" * 55)
