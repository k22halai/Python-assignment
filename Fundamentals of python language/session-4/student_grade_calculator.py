# task - 2: Student Grade Calculator (if-elif-else)

print("=" * 50)
print("              STUDENT GRADE CALCULATOR            ")
print("=" * 50)

# Taking marks as input
marks_input = input("Enter your marks (0 - 100): ")
marks = float(marks_input)

print("-" * 50)

# Validating input range and determining grade using if-elif-else
if marks < 0 or marks > 100:
    print("Invalid Input: Marks must be between 0 and 100.")
elif marks >= 90:
    print(f"Marks: {marks} | Grade: 'A' (Outstanding)")
elif marks >= 75:
    print(f"Marks: {marks} | Grade: 'B' (Very Good)")
elif marks >= 60:
    print(f"Marks: {marks} | Grade: 'C' (Good)")
elif marks >= 40:
    print(f"Marks: {marks} | Grade: 'D' (Pass)")
else:
    print(f"Marks: {marks} | Grade: 'F' (Fail)")

print("=" * 50)
