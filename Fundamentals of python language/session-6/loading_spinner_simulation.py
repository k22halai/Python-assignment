# task - 4: Simulated Loading Spinner (while True & break)

print("=" * 45)
print("          LOADING SPINNER SIMULATION          ")
print("=" * 45)

# Counter variable to track the number of loading attempts
spinner_count = 0

# Infinite while loop simulation
while True:
    print("Loading...")
    spinner_count += 1
    
    # BREAK CONDITION: Stop the infinite loop once printed 3 times
    if spinner_count == 3:
        break

print("-" * 45)
print("Content loaded successfully! (Spinner stopped)")
print("=" * 45)
