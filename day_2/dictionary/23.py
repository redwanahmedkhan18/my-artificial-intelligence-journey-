import copy


d1 = {"a": [1, 2]}
d2 = d1.copy()
d3 = copy.deepcopy(d1)

print(d1)
print(d2)
print(d3)