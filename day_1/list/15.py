#Find duplicates in list
lst=[1,2,3,4,5,3,2,1,4]
dup_lst=[]
for i in lst:
    if lst.count(i)>1 and  i not in dup_lst:
        dup_lst.append(i)

print(dup_lst)

