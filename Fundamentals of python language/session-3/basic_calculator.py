# task - 5: Basic Calculator with Operator Validation

print("=" * 50)
print("                 BASIC CALCULATOR                 ")
print("=" * 50)

# Taking input from the user
num1_input = input("Enter first number: ")
num2_input = input("Enter second number: ")
operator = input("Enter an operator (+, -, *, /): ").strip()

# Typecasting inputs to float to accommodate both integers and decimals
num1 = float(num1_input)
num2 = float(num2_input)

print("-" * 50)

# Performing operation based on the entered operator
if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    # Error message for unsupported or invalid operators
    print(f"Error: Invalid operator '{operator}'. Please use one of (+, -, *, /).")

print("=" * 50)
