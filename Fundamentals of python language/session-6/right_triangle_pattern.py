# task - 3: Right-Angled Triangle Star Pattern (while loop)

print("=" * 45)
print("     RIGHT-ANGLED TRIANGLE STAR PATTERN      ")
print("=" * 45)

total_rows = 5
current_row = 1

# Outer while loop controls the number of rows (1 to 5)
while current_row <= total_rows:
    col = 1
    # Inner while loop prints stars for the current row
    while col <= current_row:
        print("*", end="")
        col += 1
    
    # Newline after completing each row
    print()
    current_row += 1

print("=" * 45)
