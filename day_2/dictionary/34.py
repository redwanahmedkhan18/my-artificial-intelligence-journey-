#Update multiple keys at once
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

updates ={
    "name":"Redwan Ahmed Khan",
    "job":"Artificial Intelligence Engineer",
    "University":"Massachusetts Institute of Technology",
    "Salary":120000000000
}

dict_1.update(updates)

print(dict_1)

