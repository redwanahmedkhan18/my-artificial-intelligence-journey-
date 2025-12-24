#Check subset and superset
# Define two sets
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2, 6}

# Check for subset
print(f"Is set_a a subset of set_b? {set_a.issubset(set_b)}") # Output: True
print(f"Is set_c a subset of set_b? {set_c <= set_b}")      # Output: False

# Check for superset
print(f"Is set_b a superset of set_a? {set_b.issuperset(set_a)}") # Output: True
print(f"Is set_a a superset of set_c? {set_a >= set_c}")      # Output: False

# Check for proper subset/superset
print(f"Is set_a a proper subset of set_b? {set_a < set_b}") # Output: True
print(f"Is set_b a proper superset of set_a? {set_b > set_a}") # Output: True

