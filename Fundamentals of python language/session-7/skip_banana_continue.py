# task - 1: Skip Specific Item Using 'continue' Statement

fruits = ['Apple', 'Banana', 'Mango', 'Orange']

print("=" * 45)
print("         FRUITS LIST (SKIPPING BANANA)        ")
print("=" * 45)

# Iterating through the fruits list
for fruit in fruits:
    # If the fruit is 'Banana', continue statement skips the current iteration
    if fruit == 'Banana':
        continue
    
    # This print will be executed for all fruits except 'Banana'
    print(fruit)

print("=" * 45)
