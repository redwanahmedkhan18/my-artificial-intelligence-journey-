#Remove keys with None values
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
    "hobby": "AI Engineer",
    "demo":None
}

final_dict={ key: value for key, value in dict_1.items() if value is not None}
print(final_dict)