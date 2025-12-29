#Find length of each value (list) in a dictionary.
dict_1 = {
    "math": [90, 85, 88],
    "physics": [75, 80],
    "chemistry": [92, 89, 94, 90],
    "biology": []
}

lengths_of_Each_Value={}

for key,value in dict_1.items():
    lengths_of_Each_Value[key]=len(value)


print(lengths_of_Each_Value)


#better solution for mixed cases

lengths = {}

for k, v in dict_1.items():
    if isinstance(v, list):
        lengths[k] = len(v)

print(lengths)