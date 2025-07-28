grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

# 1. Slice grades from index 2 to 7
print(grades[2:7])
# Use list comprehension to find grades above 85
print([x for x in grades if x> 85])
# Replace the grade at index 3 with 95
grades[3] = 95
print('Grades with index 3 replaced',grades)
# Append three new grades
grades.extend([76,88,92])
print(grades)

# Sort in descending order and display the top 5 grades

sorted = sorted(grades, reverse=True)

print(sorted[0:5])
