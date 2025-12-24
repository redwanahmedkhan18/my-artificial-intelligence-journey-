#Find first non-repeating character 
s="My name is Redwan Ahmed Khan. I want to be an Artificial Intelligence Engineer. My journey starts from here. I want to get a remote job with a good salary within march 2026. I want to make a good career in the field of Artificial Intelligence.I want to make a comeback from my failures."

for i in range(len(s)):
    unique = True
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            unique = False
            break
    if unique:
        print(s[i])
        break
    
