
fruits_list = ["apple", "banana", "orange", "apple", "grape"]

fruits_tuple = ("apple", "banana", "orange")

fruits_set = {"apple", "banana", "orange", "grape"}

fruits_dict = {"apple": 5, "banana": 3, "orange": 8, "grape": 2}


# 1. Check for Membership

# Test whether "apple" is present in each data structure.

# # list
# print("apple" in fruits_list)

# # tuple
# print("apple" in fruits_tuple)

# # set
# print("apple" in fruits_set)

# # dict
# print("apple" in fruits_dict.keys())

# 2. Find Length

# Display the number of elements in each structure using len().


# # list
# print(len(fruits_list))

# # tuple
# print(len(fruits_tuple))

# # set
# print(len(fruits_set))

# # dict
# print(len(fruits_dict))


# 3. Iterate and Print Elements

# Loop through each structure and print its contents.
print("List____________________________________")
for i in fruits_list:
    print(i)

print("tuple____________________________________")

for i in fruits_tuple:
    print(i)

print("set____________________________________")
for i in fruits_set:
    print(i)

print("dict____________________________________")
for (i,j) in fruits_dict.items():
    print(i,j)

# 4. Compare Membership Testing Performance

# Briefly explain which data structures are more efficient for membership checks and why.

'''
Set is the most efficient for membership checks:

Time complexity: O(1) average case
Why: Uses hash table implementation, allowing direct lookup by hash value
Best for: When you need frequent membership checks and don't need duplicates or ordering

Dictionary is equally efficient for key lookups:

Time complexity: O(1) average case for keys
Why: Also uses hash table for keys
Note: Checking values is O(n) since it must scan all values

List and Tuple are less efficient:

Time complexity: O(n) - must scan through elements sequentially
Why: No indexing mechanism for arbitrary values
When to use: When you need ordering, indexing, or allow duplicates

Quick comparison for 1 million lookups:

Set/Dict keys: ~0.1 seconds
List/Tuple: ~50+ seconds (for elements at the end)

Rule of thumb: If your primary need is membership checking, convert to a set first:


'''
