# Find second largest element
lst = [1, 2, 3, 4, 5, 44, 34, 35, 23, 11, 33]

first_max=max(lst)

second_max=lst[0]

for i in lst:
    if i >second_max and i<first_max:
        second_max=i


print(second_max)
# Using built-in functions
unique_lst=list(set(lst))
unique_lst.remove(first_max)
print(max(unique_lst))
