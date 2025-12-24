#Find missing number from 1–n
lst=[1,2,3,4,6,7,8,9,10]
n=10

sums=n*(n+1)//2

for i in lst:
    sums-=i

print(sums)

print(sum(range(1, n+1)) - sum(lst))
