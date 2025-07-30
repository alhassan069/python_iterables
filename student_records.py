students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]



# Find the Student with the Highest Grade
# Identify and print the student who has the highest grade from the list.

highest_grade = students[0]
new_list = []
for student in students:
    (student_id, name, grade, age) = student
    new_list.append((name,grade))
    if grade > highest_grade[2]:
        highest_grade = student
print(highest_grade)



# Create a Name-Grade List
# Generate a new list containing only the name and grade of each student in the format: ("Alice", 85).
print(new_list)



# Demonstrate Tuple Immutability
# Attempt to change the grade of a student in the original list and show why this is not allowed with tuples.
#  Explain briefly why tuples are preferred for immutable records like student data.


try:
    students[0][1] = "Alicia"
except Exception as e:
    print(e)

# Tuples are preferred for immutable records because it does not support item assignment.
