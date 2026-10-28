# task - 5: Pyramid Star Pattern (Nested while loops for spaces & stars)

print("=" * 50)
print("     PYRAMID STAR PATTERN (BOOKMYSHOW ROWS)       ")
print("=" * 50)

total_rows = 4
current_row = 1

# Outer while loop controls the rows (1 to 4)
while current_row <= total_rows:
    # 1. First nested while loop: prints leading spaces
    spaces = total_rows - current_row
    space_count = 1
    while space_count <= spaces:
        print(" ", end="")
        space_count += 1
    
    # 2. Second nested while loop: prints odd number of stars (1, 3, 5, 7)
    stars = (2 * current_row) - 1
    star_count = 1
    while star_count <= stars:
        print("*", end="")
        star_count += 1
    
    # Move to the next line for the next row
    print()
    current_row += 1

print("=" * 50)
