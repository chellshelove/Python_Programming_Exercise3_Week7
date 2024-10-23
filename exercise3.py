# Initialize a dictionary to store student names and their scores
students_scores = {
    "Alice": (85, 92, 78),  # (Math, Science, History)
    "Bob": (90, 88, 95),
    "Charlie": (78, 82, 89)
}

# Function to calculate the total score for a student
def total_score(scores):
    return sum(scores)

# Find the student with the highest total score
highest_scorer = max(students_scores, key=lambda student: total_score(students_scores[student]))

# Print the name of the student with the highest score
print(f"The student with the highest score is: {highest_scorer}")