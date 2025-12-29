dict_1={}

dict_1={
    "name":"Redwan",
    "Age":25,
    "dept":"AI"
}

dict_1["University"]="MIT"

dict_1["name"]="Redwan Ahmed Khan"

print(dict_1)


dict_2=dict_1.copy()
print(dict_2)

for key, value in dict_1.items():
    print(key, value)