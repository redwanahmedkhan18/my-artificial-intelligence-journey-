# 3️⃣ Min–Max Finder

# Goal: Multiple outputs + *args

# Task:
# Return minimum and maximum from inputs.

# min_max(5, 2, 9, 1) → (1, 9)


# 💡 Skill: Variable inputs → structured outputs

def min_max(*args):
    maximum=max(args)
    minimum=min(args)

    return minimum,maximum

print(min_max(5, 2, 9, 1))