# Initialize an empty dictionary to store student names and their scores
students_scores = {}

# Collect names and their math, science, and history scores for three students
for i in range(3):
    name = input(f"Enter the name of student {i+1}: ")
    math_score = int(input(f"Enter {name}'s Math score: "))
    science_score = int(input(f"Enter {name}'s Science score: "))
    history_score = int(input(f"Enter {name}'s History score: "))
    
    # Store the scores as a tuple (math, science, history) in the dictionary
    students_scores[name] = (math_score, science_score, history_score)

# Function to calculate the total score for a student
def total_score(scores):
    return sum(scores)

# Find the student with the highest total score
highest_scorer = max(students_scores, key=lambda student: total_score(students_scores[student]))

# Print the name of the student with the highest score
print(f"The student with the highest score is: {highest_scorer}")