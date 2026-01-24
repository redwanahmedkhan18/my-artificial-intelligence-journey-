# User Data Extractor

# Goal: Working with dictionaries

# Task:
# Given a user dictionary, extract safe info.

# get_user_summary(user)
# # → "Redwan (25 years old)"

# Rules:

# Missing keys → handle gracefully

# 💡 Skill: Robust function design

def get_user_summary(user):
    name = user.get("name", "Unknown")
    age = user.get("age", 0)
    return f"{name} ({age} years old)"


print(get_user_summary({"name": "Redwan", "age": 25}))




def personal_info(user_info):
    name= user_info.get("name","Unknown")
    age=user_info.get("age",0)

    return f"{name}  ({age}) years old"


print(personal_info({"name":"Redwan","age":26}))

