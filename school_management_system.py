school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve",94), ("Frank", 82)]
    }
}


# Print Teacher Names
# Iterate through all classes and print the name of each teacher.
for key, value in school.items():
    print(value["teacher"])



# Calculate Class Average Grades
# For each class, calculate and display the average grade of the students.

for key, value in school.items():
    total = 0
    n = len(value["students"])

    for (name, marks) in value["students"]:
        total += marks
    print("Average grade:", total/n)



# Find Top Student Across All Classes
# Identify the student with the highest grade among all students across every class.

highest_grade = ["",0]
for key, value in school.items():

    for (name, marks) in value["students"]:
        if marks > highest_grade[1]:
            highest_grade[0] = name
            highest_grade[1] = marks

print("Highest Grade:",highest_grade)

# Use Unpacking
# Use tuple unpacking to extract and work with student names and grades separately.
