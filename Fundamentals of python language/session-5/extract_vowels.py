# task - 4: Extract and Print Vowels (for loop with multiple == checks)

print("=" * 55)
print("              EXTRACT VOWELS FROM WORD              ")
print("=" * 55)

# Prompting user for a word / song title
user_input = input("Enter a word or song name: ").strip()

print(f"\nVowels found in '{user_input}':")
print("-" * 55)

# Iterating through each character using a for loop
for char in user_input:
    # Converting character to lowercase for case-insensitive check
    lower_char = char.lower()
    
    # CONSTRAINT: Do NOT use the 'in' operator inside the if statement.
    # Using multiple '==' checks with logical 'or' instead.
    if (lower_char == 'a' or 
        lower_char == 'e' or 
        lower_char == 'i' or 
        lower_char == 'o' or 
        lower_char == 'u'):
        print(char)

print("=" * 55)
