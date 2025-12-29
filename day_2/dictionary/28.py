dict_1={
    "name":"RAK",
    "age":26,
    "city":"california",
    "job":"software engineer",
    "previous job":"software engineer"
}

dict_2={}

values=set()

for key,value in dict_1.items():
    if value not in values:
        dict_2[key]=value
        values.add(value)



print(dict_2)
