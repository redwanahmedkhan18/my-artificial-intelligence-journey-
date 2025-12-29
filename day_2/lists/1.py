# ==============================
# Python Lists Comprehensive Program
# Covers: basics, methods, operations, advanced topics
# ==============================

# ------------------------------
# 1. Creating Lists
# ------------------------------
# Lists can store elements of different types
list_a = [1, 2, 3, 4, 5]
print("List A:", list_a)

# Using list() constructor
list_b = list([3, 4, 5, 6])
print("List B:", list_b)

# Empty list
empty_list = []
print("Empty list:", empty_list)


# ------------------------------
# 2. Accessing Elements
# ------------------------------
print("First element of List A:", list_a[0])     # Indexing
print("Last element of List A:", list_a[-1])     # Negative indexing
print("Slice List A [1:4]:", list_a[1:4])       # Slicing
print("Slice List A [::2]:", list_a[::2])       # Step slicing


# ------------------------------
# 3. Adding Elements
# ------------------------------
list_a.append(6)              # Add single element at end
print("After append 6:", list_a)

list_a.extend([7, 8, 9])      # Add multiple elements at end
print("After extend [7,8,9]:", list_a)

list_a.insert(0, 0)           # Insert element at index
print("After insert 0 at index 0:", list_a)


# ------------------------------
# 4. Removing Elements
# ------------------------------
list_a.remove(0)              # Remove first occurrence of value
print("After remove 0:", list_a)

popped_element = list_a.pop() # Remove last element by default
print("Popped element:", popped_element)
print("List after pop:", list_a)

popped_index = list_a.pop(2)  # Remove element at index 2
print("Popped index 2 element:", popped_index)
print("List after pop index 2:", list_a)

list_a.clear()                # Remove all elements
print("After clear:", list_a)


# ------------------------------
# 5. Searching Elements
# ------------------------------
list_c = [1, 2, 3, 4, 3, 5]
print("List C:", list_c)
print("Index of first 3:", list_c.index(3))     # Index of first occurrence
print("Count of 3 in list:", list_c.count(3))   # Count occurrences


# ------------------------------
# 6. Sorting and Reversing
# ------------------------------
list_d = [5, 2, 9, 1, 5, 6]
list_d.sort()                  # Sort ascending
print("Sorted list:", list_d)

list_d.sort(reverse=True)      # Sort descending
print("Sorted descending:", list_d)

list_d.reverse()               # Reverse list in-place
print("Reversed list:", list_d)

# Using sorted() returns a new list
sorted_list = sorted(list_d)
print("Sorted copy using sorted():", sorted_list)


# ------------------------------
# 7. Copying Lists
# ------------------------------
original_list = [1, 2, 3]
shallow_copy = original_list.copy()    # Shallow copy
print("Shallow copy:", shallow_copy)

# Deep copy example (nested list)
import copy
nested_list = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested_list)
print("Nested list:", nested_list)
print("Deep copy:", deep_copy)


# ------------------------------
# 8. List Comprehensions
# ------------------------------
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Conditional list comprehension
even_squares = [x**2 for x in range(10) if x%2==0]
print("Even squares:", even_squares)

# Nested comprehension
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
print("3x3 multiplication matrix:", matrix)


# ------------------------------
# 9. Iterating Lists
# ------------------------------
for item in list_c:
    print("Item:", item)

for index, value in enumerate(list_c):
    print(f"Index {index} has value {value}")


# ------------------------------
# 10. Combining Lists
# ------------------------------
list1 = [1, 2]
list2 = [3, 4]

combined = list1 + list2     # Concatenation
print("Combined list:", combined)

list1.extend(list2)          # Extend list1 in-place
print("List1 after extend:", list1)


# ------------------------------
# 11. Advanced Techniques
# ------------------------------

# Flatten a nested list using list comprehension
nested = [[1,2],[3,4],[5,6]]
flattened = [item for sublist in nested for item in sublist]
print("Flattened list:", flattened)

# Filter using list comprehension
data = [10, 15, 20, 25]
filtered = [x for x in data if x>15]
print("Filtered list (x>15):", filtered)

# Map/transform using comprehension
transformed = [x*2 for x in data]
print("Transformed list (*2):", transformed)

# Using map and filter functions
mapped = list(map(lambda x: x*3, data))
filtered2 = list(filter(lambda x: x>15, data))
print("Mapped using map():", mapped)
print("Filtered using filter():", filtered2)


# ------------------------------
# 12. List Unpacking
# ------------------------------
a, b, *rest = [1, 2, 3, 4, 5]
print("a:", a, "b:", b, "rest:", rest)

# Swap values
x, y = 10, 20
x, y = y, x
print("Swapped x, y:", x, y)


# ------------------------------
# 13. Real-World Examples
# ------------------------------

# Remove duplicates while preserving order
nums = [1,2,2,3,4,4,5]
unique_ordered = list(dict.fromkeys(nums))
print("Unique ordered:", unique_ordered)

# Transpose a matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transpose of matrix:", transpose)

# Find common elements between lists
list_a = [1,2,3,4]
list_b = [3,4,5,6]
common = list(set(list_a) & set(list_b))
print("Common elements:", common)


# ------------------------------
# 14. All Methods Demonstrated
# ------------------------------
example_list = [1, 2, 3, 4]

# Adding
example_list.append(5)
example_list.extend([6,7])
example_list.insert(0,0)

# Removing
example_list.remove(0)
example_list.pop()
example_list.clear()  # Clears all elements

# Searching
example_list = [1,2,3,2,4]
example_list.index(2)
example_list.count(2)

# Sorting/Reversing
example_list.sort()
example_list.sort(reverse=True)
example_list.reverse()
sorted_copy = sorted(example_list)

# Copy
copied_list = example_list.copy()
deep_copied_list = copy.deepcopy([[1,2],[3,4]])

print("All list methods demonstrated successfully.")
