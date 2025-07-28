employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Carol", 55000, "Engineering"),
    ("David", 45000, "Sales"),
    ("Ethan", 95000, "Sales")
]


# Sort by Salary
sorted_salary = sorted(employees, key= lambda employee: employee[1])

# print(sorted_salary)

# Sort the list of employees by salary in both ascending and descending order.
reverse_sorted_salary = sorted(employees, key = lambda employee: employee[1], reverse=True)
# print(reverse_sorted_salary)


# Sort by Department, Then by Salary
# First sort by department name alphabetically, then by salary within each department.

sorted_department_salary = sorted(employees, key= lambda employee: (employee[2], employee[1]))
# print(sorted_department_salary)


# Create a Reversed List

# Reverse the order of the original list of employees without modifying the original.

reversed = employees[::-1]
# print(reversed)


# Sort by Name Length
# Sort employees based on the length of their names.

sorted_by_name_length = sorted(employees, key= lambda emp: len(emp[0]))

# print(sorted_by_name_length)



# Use sorted() vs .sort() Appropriately

# Use .sort() when modifying the original list and sorted() when creating a new sorted list. Demonstrate both methods.

employees.sort(key=lambda x: x[1])
print(employees)

print(sorted(employees,key=lambda x : len(x[2])))
