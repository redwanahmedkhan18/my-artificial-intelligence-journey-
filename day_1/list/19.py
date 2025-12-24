#Sort list without using sort 

lst=[64, 34, 25, 12, 22, 11, 90]

for i in range(len(lst)):
    for j in range(0,len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]



print(lst) 