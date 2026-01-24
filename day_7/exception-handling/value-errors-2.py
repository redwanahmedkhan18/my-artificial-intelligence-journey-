def get_integer(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return None

num = get_integer("Enter a number: ")

if num is not None:
    print("You entered:", num)
