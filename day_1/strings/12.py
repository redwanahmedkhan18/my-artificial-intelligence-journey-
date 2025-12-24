# Find longest word in a sentence
s="My name is Redwan Ahmed Khan. I want to be an Artificial Intelligence Engineer. My journey starts from here."

words=s.split()

longest_word=""

for word in words:
    if len(word)> len(longest_word):
        longest_word=word


print(longest_word)