try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(result)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")