#Move all zeros to end
lst=[0,1,0,3,12]
non_zero_lst=[]

zero_lst=[]

for i in lst:
    if i!=0:
        non_zero_lst.append(i)
    else:
        zero_lst.append(i)


new_updated_lst=non_zero_lst+zero_lst

print(new_updated_lst)

#better way

for i in range(len(lst)):
    if lst[i] != 0:
        lst[insert_pos] = lst[i]
        insert_pos += 1

# Fill remaining positions with 0
for i in range(insert_pos, len(lst)):
    lst[i] = 0

print(lst)
