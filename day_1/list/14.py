# Find all pairs with sum = k
lst=[1,2,3,4,5,6,7,8,9]
k=10
pairs=[]

for i in range(len(lst)):
    for j in range(i+1,(len(lst))):
        if lst[i]+lst[j]==k:
            pairs.append((lst[i],lst[j]))



print(pairs)

