#Count unique words in sentence
sentence="This is a sample sentence with several words This is a test sentence"
words=sentence.split()
unique_words=set(words)
print(f"Number of unique words: {len(unique_words)}")