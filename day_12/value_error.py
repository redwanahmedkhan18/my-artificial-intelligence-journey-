try:
    s=int("abc")
except ValueError as v:
    print("Invalid type conversion")

else:
    s=int(input("Enter Integer"))
    print(s**2)

finally:
    print("Value Error")