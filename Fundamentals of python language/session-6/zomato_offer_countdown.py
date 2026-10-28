# task - 2: Zomato Offer Countdown (while loop decrement)

print("=" * 45)
print("         ZOMATO OFFER COUNTDOWN         ")
print("=" * 45)

# Starting countdown variable set to 5
minutes_left = 5

# While loop running until minutes_left reaches 0
while minutes_left >= 0:
    print(f"Offer ends in {minutes_left} minutes")
    minutes_left -= 1  # Decrementing by 1 each iteration

print("-" * 45)
print("Hurry! The offer has now expired.")
print("=" * 45)
