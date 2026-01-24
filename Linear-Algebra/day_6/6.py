def safe_divide(number1,number2):
    if number2 !=0:
        return number1/number2

    else:
        return "Cannot divide by zero"
    

print(safe_divide(10,2))
    
print(safe_divide(5,0))

