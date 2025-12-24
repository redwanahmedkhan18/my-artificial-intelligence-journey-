#Reverse a list
lst=[1,2,3,4,5]
rev_lst=[]

for i in range(len(lst)-1,-1,-1):
    rev_lst.append(lst[i])


print(rev_lst)

print(lst[::-1])

