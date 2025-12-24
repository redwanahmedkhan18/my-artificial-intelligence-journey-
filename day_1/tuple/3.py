#Find index of an element
tup=(1,2,3,4,5,7)

ele=5
for i in range(len(tup)):
    if tup[i]==ele:
        print("Element found at index:",i)
        break       