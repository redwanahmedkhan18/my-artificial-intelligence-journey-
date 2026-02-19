number1=int(input("Enter Number 1:"))
number2=int(input("Enter Number 2:"))

try:
    minimum=min(number1,number2)
    maximum=max(number1,number2)

    result=maximum/minimum

except ZeroDivisionError as e:
    print(f"Division can't be possible as {e} has occured. Please divide the number with more than zero")

except ValueError as v:
    print(f"Wrong Input so {v} has been found. Division Can't be possible. Please input correct value")

else:
    minimum=min(number1,number2)
    maximum=max(number1,number2)

    result=maximum/minimum

    print(f"The division of this 2 number is:{result}")

finally:
    print("Division is done")
