#Chunk list into sublists of size k
lst=[1,2,3,4,5,6,7,8,9]
k=3
chunked_lst=[lst[i:i+k] for i in range(0,len(lst),k)]
print(chunked_lst)