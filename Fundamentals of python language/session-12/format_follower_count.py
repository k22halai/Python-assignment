# task - 2: Instagram-Style Follower Formatter (format_follower_count())

def format_follower_count(count: int) -> str:
    """
    Formats a raw follower number into an Instagram-style abbreviated string.
    - Numbers >= 1,000,000 are formatted with 'M' (e.g., 1,200,000 -> '1.2M')
    - Numbers >= 1,000 are formatted with 'K' (e.g., 1,500 -> '1.5K')
    - Numbers < 1,000 are returned as regular string integers.
    """
    if count >= 1_000_000:
        val = count / 1_000_000
        # Format to 1 decimal place, strip trailing zero if whole number (e.g., 2.0M -> 2M)
        formatted = f"{val:.1f}" if val % 1 != 0 else f"{int(val)}"
        return f"{formatted}M"
    
    elif count >= 1_000:
        val = count / 1_000
        formatted = f"{val:.1f}" if val % 1 != 0 else f"{int(val)}"
        return f"{formatted}K"
    
    else:
        return str(count)


# Demonstration with various follower numbers
print("=" * 55)
print("             FOLLOWER COUNT FORMATTER             ")
print("=" * 55)

test_counts = [450, 1500, 24000, 100000, 1200000, 50000000]

for followers in test_counts:
    formatted_str = format_follower_count(followers)
    print(f"Raw Count: {followers:>10,}  -->  Formatted: '{formatted_str}'")

print("-" * 55)
# Interactive input
user_num = input("Enter a follower count to format: ")
if user_num.isdigit():
    print(f"Instagram Format: '{format_follower_count(int(user_num))}'")
print("=" * 55)
