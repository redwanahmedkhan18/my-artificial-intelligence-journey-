file = None

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: You don't have permission to read this file")

finally:
    if file:
        file.close()
        print("File closed successfully")
