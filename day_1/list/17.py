#Flatten nested list

nested_lst=[[1,2,3],[4,5],[6,7,8,9]]
flat_lst=[]
for sublist in nested_lst:
    for item in sublist:
        flat_lst.append(item)

print(flat_lst)