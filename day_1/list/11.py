#Check if list is sorted
lst=[1,2,3,4,5,6,7]
flag=True
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        flag=False
        break

if flag:
    print("List is sorted")


else:
    print("List is not sorted")
