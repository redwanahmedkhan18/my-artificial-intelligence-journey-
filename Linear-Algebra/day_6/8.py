def average(numbers):
    if not numbers:
        return None
    else:
        averages=((sum(numbers))/(len(numbers)))

        return averages
    


print(average([80,90,100]))