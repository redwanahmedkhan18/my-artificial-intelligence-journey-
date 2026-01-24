# Email Validator

# Goal: Split logic into helper functions

# Task:
# Create:

# is_valid_email(email)

# register_user(email)

# Rules:

# Email must contain @ and .

# register_user uses is_valid_email

# 💡 Skill: Functions calling functions

def is_valid_email(email):
    return '@' in email and '.' in email
    
def register_user(email):
    if is_valid_email(email):
        print("User registered with valid email:", email)
    else:
        print("Email must contain @ and .")

register_user(email="redwan@gmail.com")

register_user("redwan@123gmail")