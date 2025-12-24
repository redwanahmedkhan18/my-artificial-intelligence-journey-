#Split list into even and odd lists
lst=[1,2,3,4,5,6,7,8,9,10]
even_lst=[]

odd_lst=[]

for i in lst:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)


print("Even List:",even_lst)

print("Odd List:",odd_lst)

print([i for i in lst if i%2==0])

print([i for i in lst if i%2!=0])

