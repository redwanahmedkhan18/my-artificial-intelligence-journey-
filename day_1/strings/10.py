#Replace all vowels with *
s="I want to be an Artificial Intelligence Engineer."

s=s.lower()
vowels='aeiou'

new_s=""

for char in s:
    if char in vowels:
        new_s=new_s+"*"
    else:
        new_s=new_s+char


print(new_s)

