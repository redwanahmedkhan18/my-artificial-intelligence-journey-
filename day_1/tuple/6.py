#Find tuple with maximum sum
tup1=(1,2,3)
tup2=(4,5)
tup3=(0,0,0,0)
tuples=[tup1,tup2,tup3]
max_tup=max(tuples,key=sum)
print("Tuple with maximum sum:",max_tup)