#Find all substrings of a string
s="def"
res=[]

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        res.append(s[i:j])



print(res)