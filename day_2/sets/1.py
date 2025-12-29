# ==============================
# Python Sets Comprehensive Program
# Covers: basics, operations, methods, advanced topics
# ==============================

# ------------------------------
# 1. Creating Sets
# ------------------------------

# Using curly braces
set_a = {1, 2, 3, 4}
print("Set A:", set_a)

# Using set() constructor (duplicates removed automatically)
set_b = set([3, 4, 4, 5, 6])
print("Set B (duplicates removed):", set_b)

# Empty set ({} creates a dict, so use set())
empty_set = set()
print("Empty set:", empty_set)


# ------------------------------
# 2. Adding Elements
# ------------------------------
set_a.add(5)          # Add single element
print("After adding 5 to Set A:", set_a)

set_a.update([6, 7])  # Add multiple elements
print("After updating Set A with [6, 7]:", set_a)


# ------------------------------
# 3. Removing Elements
# ------------------------------
set_a.remove(7)       # Remove element (KeyError if not exists)
print("After removing 7 from Set A:", set_a)

set_a.discard(10)     # Remove element safely (no error if not exists)
print("After discarding 10 (no error):", set_a)

popped_element = set_a.pop()  # Remove arbitrary element
print("Popped element:", popped_element)
print("Set A after pop:", set_a)


# ------------------------------
# 4. Set Operations
# ------------------------------
set_x = {1, 2, 3}
set_y = {3, 4, 5}

# Union
union_set = set_x.union(set_y)  # or set_x | set_y
print("Union:", union_set)

# Intersection
intersection_set = set_x.intersection(set_y)  # or set_x & set_y
print("Intersection:", intersection_set)

# Difference
diff_set = set_x.difference(set_y)  # or set_x - set_y
print("Difference (X - Y):", diff_set)

# Symmetric Difference
sym_diff = set_x.symmetric_difference(set_y)  # or set_x ^ set_y
print("Symmetric Difference:", sym_diff)


# ------------------------------
# 5. Membership Testing
# ------------------------------
print("2 in set_x?", 2 in set_x)
print("5 not in set_x?", 5 not in set_x)


# ------------------------------
# 6. Set Comprehensions
# ------------------------------
squares = {x**2 for x in range(10)}
print("Squares (set comprehension):", squares)


# ------------------------------
# 7. Subset, Superset, Disjoint
# ------------------------------
a = {1, 2}
b = {1, 2, 3, 4}

print("Is a subset of b?", a.issubset(b))        # True
print("Is b superset of a?", b.issuperset(a))    # True

c = {5, 6}
print("Is a disjoint with c?", a.isdisjoint(c))  # True


# ------------------------------
# 8. Copying Sets
# ------------------------------
original_set = {1, 2, 3}
copied_set = original_set.copy()
copied_set.add(4)
print("Original set:", original_set)
print("Copied set:", copied_set)


# ------------------------------
# 9. Frozensets (Immutable Sets)
# ------------------------------
fs = frozenset([1, 2, 3, 2])
print("Frozenset:", fs)
# fs.add(4)  # Error: cannot add to frozenset


# ------------------------------
# 10. Real-World Examples
# ------------------------------

# Remove duplicates from list
nums = [1, 2, 2, 3, 4, 4]
unique_nums = list(set(nums))
print("Unique numbers from list:", unique_nums)

# Count unique words
sentence = "this is a test this is only a test"
unique_words = set(sentence.split())
print("Unique words in sentence:", unique_words)
print("Count of unique words:", len(unique_words))

# Common elements between lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)

# Filter data using a set
data = ['apple', 'banana', 'cherry', 'apple']
allowed = {'apple', 'cherry'}
filtered = [x for x in data if x in allowed]
print("Filtered data:", filtered)


# ------------------------------
# 11. Advanced Set Techniques
# ------------------------------

# Set operations on multiple sets
sets_list = [{1, 2, 3}, {2, 3, 4}, {2, 5}]
common_multi = set.intersection(*sets_list)
print("Common elements in multiple sets:", common_multi)

# Using sets with dictionaries
d = {'a': 1, 'b': 2, 'c': 1}
unique_values = set(d.values())
print("Unique values in dictionary:", unique_values)

# Prime number sieve using sets
numbers = set(range(2, 20))
for i in range(2, 20):
    numbers -= set(range(i*2, 20, i))
print("Primes less than 20 using set sieve:", numbers)


# ------------------------------
# 12. All Methods Demonstrated
# ------------------------------
example_set = {1, 2, 3, 4}

# Add, Update
example_set.add(5)
example_set.update([6, 7])

# Remove, Discard, Pop
example_set.remove(7)
example_set.discard(10)
example_set.pop()

# Union, Intersection, Difference, Symmetric Difference
union_example = example_set.union({8, 9})
intersection_example = example_set.intersection({3, 4, 5})
difference_example = example_set.difference({1, 2})
sym_diff_example = example_set.symmetric_difference({2, 3})

# Subset, Superset, Disjoint
subset_check = {1, 2}.issubset(example_set)
superset_check = example_set.issuperset({1, 2})
disjoint_check = example_set.isdisjoint({100, 200})

# Copy
copy_set = example_set.copy()

# Frozenset
fs_example = frozenset([1, 2, 3])

print("All methods demonstrated successfully.")
