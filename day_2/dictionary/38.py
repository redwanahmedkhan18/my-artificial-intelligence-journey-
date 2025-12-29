#Find duplicate values
dict_1 = {
    "name": "RAK",
    "age": "26",
    "city": "california",
    "job": "AI Engineer",
    "company": "Google",
    "University": "MIT",
    "country": "Bangladesh",
    "Year": "2026",
    "Intended Program": "PhD in Artificial Intelligence",
    "Salary": "100000000000",
    "hobby": "AI Engineer"
}

duplicate_values_count ={}

for value in dict_1.values():
    if value in duplicate_values_count:
        duplicate_values_count[value]+=1
    else:
        duplicate_values_count[value]=1

duplicates = {value: count for value, count in duplicate_values_count.items() if count > 1}


print(duplicates)