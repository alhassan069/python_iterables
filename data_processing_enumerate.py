students = ["Alice", "Bob","Carol", "David", "Eve"]
scores = [85, 92, 78, 88, 95]

# Create a Numbered List of Students
# Print each student’s name with a number starting from 1 (e.g., 1. Alice).
for index, student in enumerate(students):
    print(f"{index + 1}: {student}")


# Pair Students with Their Scores Using enumerate()
# Combine both lists to display each student's name alongside their score.
for index, student in enumerate(students):
    print(f"{index + 1} {student}: {scores[index]}")


# Find Positions of High Scorers
# Identify and print the positions (indices) of students who scored above 90.
for index, student in enumerate(students):
    if scores[index] > 90:
        print(f"{index}")


# Map Positions to Student Names
# Create a dictionary where keys are positions (starting from 0) and values are the student names.
dct = {}
for index, student in enumerate(students):
    dct[index] = student


print(dct)
