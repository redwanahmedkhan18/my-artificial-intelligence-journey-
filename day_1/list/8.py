#Find common elements between two lists
lst1=[1,2,3,4,5,6]
lst2=[4,5,6,7,8,9]
commn_lst=[]

for i in lst1:
    if i in lst2:
        commn_lst.append(i)


print(commn_lst)

print(list(set(lst1) & set(lst2)))