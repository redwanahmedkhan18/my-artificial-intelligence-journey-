# Decode compressed string (a3b2 → aaabb)
s="a3b2c4d1a2"
decoded=""
i=0
while i<len(s):
    char=s[i]
    i+=1
    count=""
    while i<len(s) and s[i].isdigit():
        count+=s[i]
        i+=1
    decoded+=char*int(count)
print(decoded)  