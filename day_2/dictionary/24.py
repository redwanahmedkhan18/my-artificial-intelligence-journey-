#Merge two dictionaries
dict_1={}

dict_1={
    "name":"Redwan",
    "Age":25,
    "dept":"AI"
}

dict_2={
    "University":"MIT",
    "year":2026,
    "semester":"Fall-2026",
    "Goal":"To become a successful AI engineer in Google"
}

dict_1.update(dict_2)

print("After merging two dictionaries:",dict_1)
