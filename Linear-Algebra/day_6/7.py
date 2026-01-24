def format_name(first="redwan", last="ahmed", uppercase=False):
    full_name = f"{first} {last}"
    if uppercase:
        full_name = full_name.upper()
    return full_name

print(format_name())  # redwan ahmed (default)
print(format_name(first="Redwan", last="Ahmed"))  # Redwan Ahmed
print(format_name(first="Redwan", last="Ahmed", uppercase=True))  # REDWAN AHMED
print(format_name(uppercase=True))  # REDWAN AHMED (using defaults)

