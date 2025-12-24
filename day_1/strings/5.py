#Count vowels and consonants
s="I want to be an Artificial Intelligence Engineer."

s.lower()

s1='aeiou'

count_vowel=0
count_consonant=0

for char in s:
    if char in s1:
        count_vowel+=1
    elif char.isalpha():
        count_consonant+=1


print("Number of vowels:",count_vowel)

print("Number of consonants:",count_consonant)