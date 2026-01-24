# Data Transformer

# Goal: Optional behavior toggles

# Task:
# Transform numeric inputs.

# transform(1, 2, 3, scale=10, offset=5)
# # → [15, 25, 35]


# Formula:

# new_value = value * scale + offset


# Defaults:

# scale = 1

# offset = 0

# 💡 ML preprocessing vibes


def transform (numbers,scale=1,offset=0):
    new_value=[]
    for i in numbers:
        new_value.append(i*scale+offset)

    return new_value


print(transform([1, 2, 3]))                    # [1, 2, 3]
print(transform([1, 2, 3], scale=10, offset=5)) # [15, 25, 35]
print(transform([15, 25, 35], scale=1, offset=0)) # [15, 25, 35]



