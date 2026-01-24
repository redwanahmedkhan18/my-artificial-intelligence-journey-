# 1️⃣5️⃣ Data Normalizer

# Goal: Practical ML-style function

# Task:
# Normalize numbers between 0 and 1.

# normalize([10, 20, 30]) → [0.0, 0.5, 1.0]


# 💡 Skill: Data preprocessing logic


def normalize(numbers):
    max_n=max(numbers)

    min_n=min(numbers)

    lst=[]
    if max_n == min_n:
        return [0.0 for _ in numbers]

    else:
        for i in numbers:
            lst.append((i-min_n)/(max_n-min_n))

    
    return lst

print(normalize([10, 20, 30]))

print(normalize([5,5,5]))


#normalization using numpy


import numpy as np

def normalize_numpy(arr):
    arr = np.array(arr, dtype=float)

    min_val= arr.min()
    max_val = arr.max()

    if max_val == min_val:
        return np.zeros_like(arr)

    return (arr - min_val) / (max_val - min_val)



print(normalize_numpy([10, 20, 30]))
