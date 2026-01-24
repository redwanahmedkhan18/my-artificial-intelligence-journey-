# Average Calculator (Robust)

# Goal: Combine validation + *args

# Task:
# Calculate average of given numbers.

# average(10, 20, 30) → 20
# average() → None
# 💡 Skill: Handling empty input gracefully


def average(*args):
    if not args:
        return None
    return sum(args) / len(args)
print(average(10, 20, 30))
print(average())