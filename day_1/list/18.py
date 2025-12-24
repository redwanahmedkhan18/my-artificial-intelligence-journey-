#Remove element at even indices
lst=[10,20,30,40,50,60,70,80,90,100]

new_lst=[]
for i in range(len(lst)):
    if i%2!=0:
        new_lst.append(lst[i])


print(new_lst)

