#Word frequency from paragraph

paragraph = """In computer science, a dictionary is a data structure that stores data in key-value pairs. Each key is unique and is used to access the corresponding value. Dictionaries are commonly used for efficient data retrieval and manipulation. They are implemented in various programming languages, including Python, where they are known as 'dict'. Dictionaries provide fast lookups, insertions, and deletions of key-value pairs, making them a versatile and powerful tool for managing data."""

word_list = paragraph.split()
word_frequency = {}
for word in word_list:
    word = word.strip('.,()\'"').lower()  
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print(word_frequency)