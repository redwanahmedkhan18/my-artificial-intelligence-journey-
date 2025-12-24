#Count occurrences of an element
lst=[1,2,3,4,5,3,2,1,4]

element=3

count=0

for i in lst:
    if i==element:
        count+=1

print("Count without built-in:",count)


print(lst.count(element))