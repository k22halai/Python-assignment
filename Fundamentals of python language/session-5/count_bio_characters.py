# task - 2: Count Bio Characters Excluding Spaces (for loop & conditional)

# Given string
user_bio = 'Music lover | Foodie | Traveller'

# Counter variable to store non-space character count
character_count = 0

# Iterating through each character using a for loop
for char in user_bio:
    # Using an if statement to skip spaces and count only non-space characters
    if char != ' ':
        character_count += 1

print("=" * 50)
print("            BIO CHARACTER COUNTER            ")
print("=" * 50)
print(f"User Bio: \"{user_bio}\"")
print(f"Total Characters (excluding spaces): {character_count}")
print("=" * 50)
