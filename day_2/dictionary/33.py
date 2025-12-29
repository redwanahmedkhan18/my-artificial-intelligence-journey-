#Reverse key‑value pairs in a dictionary.

dict_1={
    "name":"RAK",
    "age":"26",
    "city":"california",
    "job":"AI Engineer",
    "company":"Google",
    "University":"MIT",
    "country":"Bangladesh",
    "Year":"2026",
    "Intended Program":"PhD in Artificial Intelligence",
    "Salary":"100000000000"
}


reversed_dict={}

for key,value in dict_1.items():
    reversed_dict.setdefault(value, []).append(key)


print(reversed_dict)