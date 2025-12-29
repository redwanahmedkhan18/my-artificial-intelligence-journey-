# ==============================
# Python Strings Comprehensive Program
# Covers: basics, operations, methods, advanced topics
# ==============================

# ------------------------------
# 1. Creating Strings
# ------------------------------
str1 = "Hello, World!"                  # Double quotes
str2 = 'Python is awesome'              # Single quotes
str3 = """This is a 
multi-line string"""                    # Triple quotes
str4 = '''Another multi-line string'''  # Triple single quotes

print(str1, str2, str3, str4)

# Empty string
empty_str = ""
print("Empty string:", empty_str)

# Using str() constructor
num = 123
str_num = str(num)
print("String from number:", str_num)


# ------------------------------
# 2. Accessing Characters
# ------------------------------
s = "Python"

print("First character:", s[0])
print("Last character:", s[-1])
print("Slice s[0:4]:", s[0:4])        # 0 to 3
print("Slice s[::2]:", s[::2])        # Every 2nd character
print("Reversed string:", s[::-1])    # Reverse


# ------------------------------
# 3. String Immutability
# ------------------------------
# Strings are immutable, cannot assign to indices
# s[0] = "p"  # Uncommenting this will raise TypeError

# But can create new string
new_s = "p" + s[1:]
print("Modified string:", new_s)


# ------------------------------
# 4. String Concatenation and Repetition
# ------------------------------
a = "Hello"
b = "World"

concat = a + " " + b
repeat = a * 3

print("Concatenated:", concat)
print("Repeated:", repeat)


# ------------------------------
# 5. String Methods (Basic)
# ------------------------------
text = "  Python Strings Example  "

print("Original text:", text)
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Title case:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())
print("Stripped text:", text.strip())        # Remove leading/trailing whitespace
print("Left strip:", text.lstrip())
print("Right strip:", text.rstrip())


# ------------------------------
# 6. Searching & Replacing
# ------------------------------
s = "Python is powerful and Python is popular"

print("Count of 'Python':", s.count("Python"))
print("Index of first 'Python':", s.find("Python"))      # -1 if not found
print("Index of first 'Python' using index():", s.index("Python"))  # Raises error if not found
print("Starts with 'Python':", s.startswith("Python"))
print("Ends with 'popular':", s.endswith("popular"))

# Replace
s_replaced = s.replace("Python", "Java")
print("Replaced string:", s_replaced)


# ------------------------------
# 7. Splitting and Joining
# ------------------------------
csv = "apple,banana,cherry"
fruits = csv.split(",")        # Split into list
print("Split fruits:", fruits)

sentence = "Python is amazing"
words = sentence.split()       # Split by whitespace
print("Words:", words)

# Join list into string
joined = "-".join(fruits)
print("Joined string:", joined)


# ------------------------------
# 8. String Formatting
# ------------------------------

# Old style % formatting
name = "Alice"
age = 25
print("Hello %s, you are %d years old" % (name, age))

# str.format() method
print("Hello {}, you are {} years old".format(name, age))
print("Hello {n}, you are {a} years old".format(n=name, a=age))

# f-strings (Python 3.6+)
print(f"Hello {name}, you are {age} years old")

# Padding and alignment
print(f"{'Left':<10} | {'Center':^10} | {'Right':>10}")


# ------------------------------
# 9. Advanced String Methods
# ------------------------------
text = "python programming"

print("isalpha():", text.isalpha())      # True if all alphabetic (False because of space)
print("isalnum():", text.isalnum())      # True if alphanumeric (False)
print("isdigit():", text.isdigit())      # True if digits only
print("islower():", text.islower())      # True if all lowercase
print("isupper():", text.isupper())      # True if all uppercase
print("istitle():", text.istitle())      # True if titlecased


# ------------------------------
# 10. Escaping Characters
# ------------------------------
escaped = "This is a line\nThis is another line\twith tab and a quote \'"
print(escaped)

# Raw strings
raw_s = r"C:\Users\name\Documents"
print("Raw string:", raw_s)


# ------------------------------
# 11. Multiline Strings
# ------------------------------
multi_line = """This is line 1
This is line 2
This is line 3"""
print(multi_line)


# ------------------------------
# 12. String Membership & Iteration
# ------------------------------
s = "Python"

print("'y' in s?", 'y' in s)
print("'z' not in s?", 'z' not in s)

for ch in s:
    print(ch, end=" ")
print()


# ------------------------------
# 13. Advanced Examples
# ------------------------------

# Reverse words in a sentence
sentence = "Python is awesome"
reversed_words = " ".join(sentence.split()[::-1])
print("Reversed words:", reversed_words)

# Remove punctuation
import string
text = "Hello!!! How are you???"
clean_text = ''.join(ch for ch in text if ch not in string.punctuation)
print("Text without punctuation:", clean_text)

# Count words frequency
sentence = "Python is fun and Python is powerful"
words = sentence.split()
freq = {word: words.count(word) for word in set(words)}
print("Word frequency:", freq)

# Palindrome check
s = "racecar"
is_palindrome = s == s[::-1]
print(f"Is '{s}' palindrome?", is_palindrome)

# Advanced formatting with numbers
pi = 3.14159265
print(f"Pi rounded to 2 decimals: {pi:.2f}")


# ------------------------------
# 14. All string methods demonstration
# ------------------------------
demo = "  Python Demo String 123!  "

print("Original:", demo)
print("lower():", demo.lower())
print("upper():", demo.upper())
print("title():", demo.title())
print("capitalize():", demo.capitalize())
print("swapcase():", demo.swapcase())
print("strip():", demo.strip())
print("lstrip():", demo.lstrip())
print("rstrip():", demo.rstrip())
print("count('n'):", demo.count('n'))
print("find('Demo'):", demo.find('Demo'))
print("replace('Python','Java'):", demo.replace("Python","Java"))
print("split():", demo.split())
print("join():", "-".join(demo.split()))
print("startswith('  P'):", demo.startswith("  P"))
print("endswith('!  '):", demo.endswith("!  "))
print("isalnum():", demo.isalnum())
print("isalpha():", demo.isalpha())
print("isdigit():", demo.isdigit())
print("islower():", demo.islower())
print("isupper():", demo.isupper())
print("istitle():", demo.istitle())

print("All string operations demonstrated successfully.")
# End of the comprehensive string program