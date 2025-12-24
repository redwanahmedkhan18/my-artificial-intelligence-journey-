#Rotate list by k steps
lst=[1,2,3,4,5,6,7]

k=3

k=k%len(lst)
rotated_lst=lst[-k:]+lst[:-k]
print(rotated_lst)