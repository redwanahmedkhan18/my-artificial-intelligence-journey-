#Count frequency of each character

s="My name is Redwan Ahmed Khan. I want to be an Artificial Intelligence Engineer. My journey starts from here. I want to get a remote job with a good salary within march 2026. I want to make a good career in the field of Artificial Intelligence.I want to make a comeback from my failures."

frequency={}

for char in s:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1


print(frequency)