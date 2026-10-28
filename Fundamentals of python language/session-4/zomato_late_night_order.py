# task - 3: Zomato Late Night Order Eligibility (Nested if-else)

print("=" * 55)
print("        ZOMATO LATE-NIGHT ORDER ELIGIBILITY CHECK       ")
print("=" * 55)

# Taking age and current time (in 24-hour format) as input
age = int(input("Enter your age: "))
current_time = int(input("Enter current time in 24-hour format (0 - 23): "))

print("-" * 55)

# Time range validation
if current_time < 0 or current_time > 23:
    print("Invalid Input: Time must be between 0 and 23.")
else:
    # NESTED IF STATEMENTS:
    # Outer if: Check age requirement (18 or above)
    if age >= 18:
        # Inner if: Check if time is between 22 (10 PM) and 2 (2 AM)
        if current_time >= 22 or current_time <= 2:
            print("Order allowed")
            print("Status: Eligible for late-night delivery service.")
        else:
            print("Order not allowed")
            print("Reason: Late-night delivery is only available between 22:00 (10 PM) and 02:00 (2 AM).")
    else:
        # Outer else: If user is under 18
        print("Order not allowed")
        print("Reason: You must be at least 18 years old to place a late-night order.")

print("=" * 55)
