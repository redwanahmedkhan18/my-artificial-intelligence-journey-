# ==============================
# Python Tuples Comprehensive Program
# Covers: basics, operations, methods, advanced topics
# ==============================

# ------------------------------
# 1. Creating Tuples
# ------------------------------
# Tuples can store elements of different types
tuple_a = (1, 2, 3, 4, 5)
print("Tuple A:", tuple_a)

# Tuple without parentheses (tuple packing)
tuple_b = 6, 7, 8
print("Tuple B:", tuple_b)

# Single element tuple (requires comma)
single_tuple = (1,)
print("Single element tuple:", single_tuple)

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Using tuple() constructor
tuple_c = tuple([1, 2, 3])
print("Tuple C:", tuple_c)


# ------------------------------
# 2. Accessing Elements
# ------------------------------
print("First element of Tuple A:", tuple_a[0])   # Indexing
print("Last element of Tuple A:", tuple_a[-1])   # Negative indexing
print("Slice Tuple A [1:4]:", tuple_a[1:4])     # Slicing
print("Slice Tuple A [::2]:", tuple_a[::2])     # Step slicing


# ------------------------------
# 3. Tuple Immutability
# ------------------------------
# Tuples are immutable: elements cannot be changed
# tuple_a[0] = 10  # Uncommenting this will raise TypeError

# However, mutable elements inside a tuple can be changed
tuple_with_list = (1, 2, [3, 4])
tuple_with_list[2].append(5)
print("Tuple with mutable list changed:", tuple_with_list)


# ------------------------------
# 4. Tuple Operations
# ------------------------------
tuple_x = (1, 2, 3)
tuple_y = (3, 4, 5)

# Concatenation
concat_tuple = tuple_x + tuple_y
print("Concatenated tuple:", concat_tuple)

# Repetition
repeat_tuple = tuple_x * 2
print("Repeated tuple:", repeat_tuple)

# Membership testing
print("2 in tuple_x?", 2 in tuple_x)
print("5 not in tuple_x?", 5 not in tuple_x)


# ------------------------------
# 5. Tuple Methods
# ------------------------------
tuple_example = (1, 2, 3, 2, 4)

# count() - count occurrences of a value
count_2 = tuple_example.count(2)
print("Count of 2 in tuple_example:", count_2)

# index() - first index of a value
index_3 = tuple_example.index(3)
print("Index of 3 in tuple_example:", index_3)

# Note: Tuples have only 2 built-in methods: count() and index()


# ------------------------------
# 6. Tuple Unpacking
# ------------------------------
a, b, c, d, e = tuple_example
print("Unpacked values:", a, b, c, d, e)

# Extended unpacking
x, y, *rest = tuple_example
print("x:", x, "y:", y, "rest:", rest)

# Swap values using tuple unpacking
p, q = 10, 20
p, q = q, p
print("Swapped p, q:", p, q)


# ------------------------------
# 7. Iterating Tuples
# ------------------------------
for item in tuple_example:
    print("Item:", item)

for index, value in enumerate(tuple_example):
    print(f"Index {index} has value {value}")


# ------------------------------
# 8. Nested Tuples
# ------------------------------
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)

# Access nested elements
print("First element of first nested tuple:", nested_tuple[0][0])


# ------------------------------
# 9. Converting Between Lists and Tuples
# ------------------------------
list_from_tuple = list(tuple_example)
print("List from tuple:", list_from_tuple)

tuple_from_list = tuple(list_from_tuple)
print("Tuple from list:", tuple_from_list)


# ------------------------------
# 10. Real-World Examples
# ------------------------------

# Swapping variables without temporary variable
x, y = 5, 10
x, y = y, x
print("Swapped using tuple unpacking:", x, y)

# Return multiple values from a function
def min_max(numbers):
    return min(numbers), max(numbers)

numbers = [3, 5, 1, 8, 2]
minimum, maximum = min_max(numbers)
print("Minimum and Maximum:", minimum, maximum)

# Using tuples as dictionary keys
dict_with_tuple_keys = {(1,2): "Point A", (3,4): "Point B"}
print("Dictionary with tuple keys:", dict_with_tuple_keys)


# ------------------------------
# 11. Advanced Techniques
# ------------------------------

# Nested tuple unpacking
nested = ((1,2), (3,4), (5,6))
for (x, y) in nested:
    print("x:", x, "y:", y)

# Using tuples in sorting
points = [(1,2), (3,1), (5,0), (2,3)]
sorted_points = sorted(points, key=lambda p: p[1])  # Sort by y-coordinate
print("Points sorted by y-coordinate:", sorted_points)


# ------------------------------
# 12. Demonstrating All Tuple Features Together
# ------------------------------
example_tuple = (10, 20, 30, 40, 50)

# Access
print(example_tuple[0])
print(example_tuple[-1])
print(example_tuple[1:4])

# Operations
print(example_tuple + (60,70))
print(example_tuple * 2)
print(20 in example_tuple)

# Methods
print(example_tuple.count(30))
print(example_tuple.index(40))

# Unpacking
a,b,*rest = example_tuple
print(a,b,rest)

# Converting to list and back
lst = list(example_tuple)
tup = tuple(lst)

# Nested tuple
nested = ((1,2),(3,4))
print(nested[1][1])

# Iteration
for val in example_tuple:
    print(val)

print("All tuple features demonstrated successfully.")
