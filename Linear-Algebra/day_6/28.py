num=[1,2,3,4,5,6]
numbers =list(filter(lambda x: x>0,num))

result = list(
    map(lambda x: x ** 2,
        filter(lambda x: x > 0, num))
)



print(result)