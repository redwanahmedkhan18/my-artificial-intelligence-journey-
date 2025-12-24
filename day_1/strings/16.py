#Find most frequent character

s="My name is Redwan Ahmed Khan. I want to be an Artificial Intelligence Engineer. My journey starts from here. I want to get a remote job with a good salary within march 2026. I want to make a good career in the field of Artificial Intelligence.I want to make a comeback from my failures."

char_count={}

for char in s:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1

most_frequent_char=max(char_count, key=char_count.get)

print(most_frequent_char)