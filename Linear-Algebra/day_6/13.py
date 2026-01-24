def text_stats(text):
    characters = len(text)
    
    words = text.split()
    word_count = len(words)
    
    if word_count > 0:
        avg_word_length = sum(len(word) for word in words) / word_count
    else:
        avg_word_length = 0

    return characters, word_count, avg_word_length



chars, words, avg = text_stats("Python makes life easier")

print("Total characters:", chars)
print("Total words:", words)
print("Average word length:", avg)
