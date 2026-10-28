# task - 5: Paytm-Style Phone Number Masking (Slicing & Concatenation)

def mask_phone_number(phone: str) -> str:
    """
    Takes a 10-digit phone number as a string and returns it with the 
    first 6 digits masked as '******', revealing only the last 4 digits (like Paytm).
    Uses string slicing and string concatenation.
    """
    clean_phone = phone.strip()
    
    # Validation check for 10-digit input
    if len(clean_phone) != 10 or not clean_phone.isdigit():
        return "Invalid input: Please provide a valid 10-digit numerical phone number."
    
    # Extracting the last 4 digits using negative slicing
    last_4_digits = clean_phone[-4:]
    
    # Slicing & Concatenation: Masking first 6 digits with asterisks
    masked_number = "******" + last_4_digits
    return masked_number


# Demonstration
print("=" * 55)
print("             PAYTM-STYLE PHONE MASKER             ")
print("=" * 55)

sample_numbers = [
    "9876543210",
    "9123456789",
    "9988776655"
]

for num in sample_numbers:
    masked = mask_phone_number(num)
    print(f"Original Phone: {num} -> Masked: {masked}")

print("-" * 55)
user_phone = input("Enter a 10-digit phone number: ")
print(f"Masked Result : {mask_phone_number(user_phone)}")
print("=" * 55)
