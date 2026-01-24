# Sorting with Lambdas

# Goal: Real-world lambda usage

# Task:
# Sort a list of dictionaries by age.

# users = [
#   {"name": "A", "age": 30},
#   {"name": "B", "age": 25}
# ]


# 💡 Skill: key= functions
users = [
  {"name": "A", "age": 30},
  {"name": "B", "age": 25}
]
sorted_function=sorted(users, key=lambda x: x["age"])

print(sorted_function)