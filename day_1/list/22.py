#Replace each element with product of all others
lst = [1, 2, 3, 4]
n = len(lst)
result = []

for i in range(n):
    prod = 1
    for j in range(n):
        if i != j:
            prod *= lst[j]
    result.append(prod)

print(result)
