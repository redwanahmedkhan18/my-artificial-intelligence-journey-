#Convert lowercase to uppercase (without .upper())
s="my name is redwan ahmed khan"
converted_output=""

for char in s:
    if char>='a' and char<='z':
        converted_output+=chr(ord(char)-32)
    else:
        converted_output+=char

print(converted_output)