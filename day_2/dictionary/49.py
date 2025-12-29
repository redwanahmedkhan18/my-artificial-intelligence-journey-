#Find top 3 frequent elements in a list using dictionary

lst=[1,2,3,4,5,1,2,3,1,2,1,6,7,8,9,6,5,4,3,2,1,5,6,7,8,9,0,1,2,3,4,5]

frequency_dict={}
for item in lst:
    if item in frequency_dict:
        frequency_dict[item]+=1
    else:
        frequency_dict[item]=1


#top 3 frequent elments

top_three={}

for key,value in sorted(frequency_dict.items(),key=lambda x:x[1],reverse=True)[:3]:
    top_three[key]=value

print(top_three)