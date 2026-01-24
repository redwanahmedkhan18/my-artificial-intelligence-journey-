# Password Strength Checker

# Goal: Clear rules & readable logic

# Task:
# Return "Weak", "Medium", or "Strong" based on:

# length

# digits

# uppercase letters

# 💡 Skill: Rule-based design


def pass_checker(s):
    length=len(s)

    has_digit=any(char.isdigit() for char in s)

    has_upper=any(char.isupper() for char in s)


    if length > 10 and has_digit and has_upper:
        return "Strong"
    
    elif length >7 and has_digit:
        return "Medium"
    
    else:
        return "Weak"
    


print(pass_checker("a1B2@355dff;err"))


print(pass_checker("A12455"))

print(pass_checker("A1234sdg"))

