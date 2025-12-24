#Reverse a string

s="My name is Redwan Ahmed Khan. I want to be an Artificial Intelligence Engineer. My journey starts from here."

reversed_s=""
#check=""
for char in s:
    # check=check+char
    reversed_s=char+reversed_s

print(reversed_s)

# print(check)

print(s[::-1])
