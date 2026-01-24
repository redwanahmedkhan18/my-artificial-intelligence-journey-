
try:
    x=int(input("Enter the first number:"))
    y=int(input("Enter the second number: "))
    z=y/x
    print("Result is:",z)

except ZeroDivisionError as e:
    print(e,"occurs.Numbers can't be divided by zero.")

except ValueError:
    print("wrong input . Please input correct number.")
    