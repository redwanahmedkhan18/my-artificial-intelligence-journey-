#Find longest increasing subarray
lst=[1,2,1,3,4,5,2,6,7,8]
count=1

max_count=1

for i in range(1,len(lst)):
    if lst[i]>lst[i-1]:
        count+=1
        max_count=max(max_count,count)
    else:
        count=1


print("Longest increasing subarray length is:",max_count)

