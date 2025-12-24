#reverse a string according to words

s="My name is Redwan Ahmed Khan. I want to be an Artificial Intelligence Engineer. My journey starts from here."

words = s.split()           
words.reverse()           
reversed_string = " ".join(words) 
print(reversed_string)
