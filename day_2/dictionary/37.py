#Convert dictionary to list of tuples
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

list_of_tuples=list(dict_1.items())

print(list_of_tuples)