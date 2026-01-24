def count_words(s):
    count =1
    for i in s:
        if i ==" ":
            count+=1

    return count


print(count_words("Python is really fun"))