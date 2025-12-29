#Group words by length by using dictionary only

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

length_words_dict ={}

for word in dict_1.values():
    length = len(word)
    if length not in length_words_dict:
        length_words_dict[length] = []
    length_words_dict[length].append(word)

print(length_words_dict)

