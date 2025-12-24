#Find maximum and minimum (no built-ins)

lst=[1,2,3,4,5,44,34,35,23,11,33]

max_val=lst[0]

min_val=lst[0]


for i in lst:
    if i> max_val:
     max_val=i
    
    if i< min_val:
       min_val=i
       
print(max_val)

print(min_val)

print(max(lst))

print(min(lst))
