# task - 3: Reverse Message Without Built-In reversed() or [::-1]

def reverse_message(message: str) -> str:
    """
    Reverses any string passed to it.
    CONSTRAINT: Does NOT use Python's built-in reversed() or [::-1] slicing shortcut.
    Implemented using a manual character accumulation loop.
    """
    reversed_text = ""
    
    # Iterating through the string and prepending each character
    for char in message:
        reversed_text = char + reversed_text
    
    return reversed_text


# Alternative index-based reverse without [::-1] or reversed():
def reverse_message_by_index(message: str) -> str:
    reversed_text = ""
    # Looping backwards from last index (len - 1) down to 0
    for i in range(len(message) - 1, -1, -1):
        reversed_text += message[i]
    return reversed_text


# Demonstration
print("=" * 55)
print("             REVERSE MESSAGE GENERATOR            ")
print("=" * 55)

sample_messages = [
    "Hello WhatsApp",
    "Python Programming",
    "Antigravity",
    "123456789"
]

for msg in sample_messages:
    result = reverse_message(msg)
    print(f"Original: '{msg}' -> Reversed: '{result}'")

print("-" * 55)
user_msg = input("Enter a message to reverse: ")
print(f"Reversed Message: '{reverse_message(user_msg)}'")
print("=" * 55)
