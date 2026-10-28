# task - 4: Cricket Score Evaluator (if-elif-else)

print("=" * 50)
print("             CRICKET SCORE EVALUATOR            ")
print("=" * 50)

# Taking score input from the user
team_name = input("Enter team name (e.g., India, CSK): ").strip()
score_input = input("Enter the team's score: ")
score = int(score_input)

print("-" * 50)
if team_name:
    print(f"Team : {team_name}")
print(f"Score: {score}")

# Evaluating score using if-elif-else statements
if score >= 200:
    print("High Score!")
elif score >= 150:  # Evaluates scores between 150 and 199
    print("Good Score")
elif score >= 100:  # Evaluates scores between 100 and 149
    print("Average")
else:               # Scores below 100
    print("Needs Improvement")

print("=" * 50)
