#Remove duplicates from list
lst=[1,2,3,4,5,3,2,1,4]

new_lst=[]

for i in lst:
    if i not in new_lst:
        new_lst.append(i)


print(new_lst)


print(list(set(lst)))
