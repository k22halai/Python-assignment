# task - 1: Instagram Caption Truncation (insta_caption.py)

print("=" * 50)
print("            INSTAGRAM CAPTION TRUNCATOR           ")
print("=" * 50)

# Taking Instagram caption input from the user
caption = input("Enter your Instagram caption: ")

# Accessing the first 10 characters using string indexing & slicing
first_10_chars = caption[0:10]

print("-" * 50)
print(f"Original Caption  : \"{caption}\"")
print(f"First 10 Characters: \"{first_10_chars}\"")

# Demonstrating individual character access via indexing
print("\nCharacter breakdown (indexes 0 to 9):")
for i in range(min(10, len(caption))):
    print(f"  Index [{i}] -> '{caption[i]}'")

print("=" * 50)
