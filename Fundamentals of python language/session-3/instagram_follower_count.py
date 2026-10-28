# task - 4: Instagram Follower Count (Formatting & Escape Characters)

# Prompting user for follower count
follower_input = input("Enter your Instagram follower count: ")

# Converting input to an integer
follower_count = int(follower_input)

# Printing output formatted with comma separators and \n (newline) & \t (tab) escape characters
print(f"\n\tYou have {follower_count:,} followers")
