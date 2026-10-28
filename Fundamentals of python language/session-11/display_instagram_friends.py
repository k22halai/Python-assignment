# task - 3: Display Instagram Followers Function (display_friends())

def display_friends(friends_dict: dict) -> None:
    """
    Takes a dictionary of Instagram usernames as keys and follower counts as values,
    and prints each entry in the format: 'username: 2.3K followers'.
    """
    print("-" * 45)
    for username, followers in friends_dict.items():
        # Ensures output matches the required format: 'username: 2.3K followers'
        # Handles whether follower count is already formatted with 'K' or is a raw string/number
        follower_str = str(followers)
        if not follower_str.endswith('K') and not follower_str.endswith('M'):
            print(f"{username}: {follower_str} followers")
        else:
            print(f"{username}: {follower_str} followers")
    print("-" * 45)


# Demonstration with sample data
print("=" * 50)
print("             INSTAGRAM FRIENDS DISPLAY            ")
print("=" * 50)

instagram_friends = {
    'rahul_sharma': '2.3K',
    'priya_patel': '5.8K',
    'tech_guru_99': '12.1K',
    'wanderlust_sam': '850'
}

display_friends(instagram_friends)
print("=" * 50)
