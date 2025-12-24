#Check if two strings are anagrams
s="hiboss"
s2="hssbio"
s1=sorted(s)

s3=sorted(s2)

if s1==s3 and len(s1)==len(s3):
    print("Anagram")
else:
    print(-1)