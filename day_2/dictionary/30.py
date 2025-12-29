#Sort dictionary by values

dict_1={
    1:34,
    2:35,
    3:106,
    4:45,
    5:23
}

print(sorted(dict_1.items(),key=lambda x:x[1]))