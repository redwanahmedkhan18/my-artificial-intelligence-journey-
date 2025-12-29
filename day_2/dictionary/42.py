#Implement histogram using dictionary

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
histogram = {}
for item in data:
    if item in histogram:
        histogram[item] += 1
    else:
        histogram[item] = 1

print(histogram)
