dict_1={}

dict_1={
    "name":"Redwan",
    "Age":25,
    "dept":"AI"
}

dict_1["University"]="MIT"

dict_1["name"]="Redwan Ahmed Khan"

print(dict_1)

del dict_1["Age"]

print("After deleting Age key:",dict_1)

dict_1.pop("dept")

print(dict_1)

dict_1.popitem()
print("After popitem:",dict_1)  