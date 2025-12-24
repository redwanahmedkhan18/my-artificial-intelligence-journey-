#Find majority element
lst=[3,3,4,2,4,4,2,4,4,3,3,4,4,4]
majority_count=len(lst)//2
element=None    
for i in lst:
    if lst.count(i)>majority_count:
        element=i
        break   
print("Majority element is:",element)