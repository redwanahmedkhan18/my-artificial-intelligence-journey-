#Sort tuple of tuples by second element
tup=((1,3),(2,2),(4,7),(9,3))

sorted_lst=sorted(tup,key=lambda x:x[1])
sorted_tup=tuple(sorted_lst)

print("Sorted tuple:",sorted_tup)