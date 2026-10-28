# task - 4: Filter Messages Using Both 'continue' and 'break'

messages = ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?']

print("=" * 55)
print("             MESSAGE FILTERING SYSTEM                ")
print("=" * 55)

for message in messages:
    # 1. CONTINUE: Skip printing any message that is 'Spam'
    if message == 'Spam':
        continue
    
    # 2. BREAK: Stop reading further if 'How are you?' is found
    if message == 'How are you?':
        print(f"\n[Trigger] Found '{message}' -> Stopping further reading.")
        break
    
    # Printing valid, non-spam messages
    print(f"Message: {message}")

print("=" * 55)
