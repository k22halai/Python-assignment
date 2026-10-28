# task - 1: Instagram Account Eligibility (if-else)

print("=" * 50)
print("         INSTAGRAM ACCOUNT ELIGIBILITY CHECK       ")
print("=" * 50)

# Taking age as input from the user
age_input = input("Enter your age: ")
age = int(age_input)

# Checking eligibility (must be 13 or older)
if age >= 13:
    print("\nResult: You are eligible to create an account on Instagram!")
else:
    print(f"\nResult: You are not eligible to create an account on Instagram. (Minimum age required is 13, you entered {age})")

print("=" * 50)
