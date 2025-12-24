#Remove spaces from a string

s="My name is Redwan Ahmed Khan. I want to be an Artificial Intelligence Engineer.My journey starts from December 23, 2025."

new_s=""

for char in s:
    if char!=" ":
        new_s=new_s+char


print(new_s)

print(s.replace(" ",""))
