#Count character frequency in string using dictionary 

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

char_frequency = {}

for value in dict_1.values():
    for char in value:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

print(char_frequency)