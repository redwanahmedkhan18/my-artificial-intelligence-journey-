# 1️⃣ Smart Sum

# Goal: Accept any number of numbers

# Task:
# Write a function that returns the sum of all numbers passed.

# smart_sum(1, 2, 3) → 6
# smart_sum(5, 10, 15, 20) → 50


# Rules:

# If no arguments → return 0

# Ignore non-numeric values

# 💡 Real-world use: Aggregations, metrics, logging

def smart_sum(*args):
    return sum(args)


print(smart_sum(1, 2, 3))
print(smart_sum(5, 10, 15, 20))
