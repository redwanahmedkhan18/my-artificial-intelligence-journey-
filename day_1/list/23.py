#Find leaders in list
lst=[16,17,4,3,5,2]
leaders=[]
n=len(lst)
for i in range(n):
    flag=True
    for j in range(i+1,n):
        if lst[i]<=lst[j]:
            flag=False
            break
    if flag:
        leaders.append(lst[i])
print(leaders)