# task - 2: Arithmetic Operations with Typecasting (int())

print("=" * 45)
print("             ARITHMETIC OPERATIONS            ")
print("=" * 45)

# Taking string inputs from user
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

# Typecasting input strings to integers
num1 = int(num1_str)
num2 = int(num2_str)

# Performing arithmetic calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print("\n--- Results ---")
print(f"Sum (Addition)        : {num1} + {num2} = {addition}")
print(f"Difference (Subtraction): {num1} - {num2} = {subtraction}")
print(f"Product (Multiplication): {num1} * {num2} = {multiplication}")

# Checking for division by zero before calculating quotient
if num2 != 0:
    quotient = num1 / num2
    print(f"Quotient (Division)    : {num1} / {num2} = {quotient:.2f}")
else:
    print("Quotient (Division)    : Cannot divide by zero!")

print("=" * 45)
