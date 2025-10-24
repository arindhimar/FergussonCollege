s = "raaaajj"

l=len(s)


freq={}

for i in range(l):
    if s[i] in freq:
        freq[s[i]]+=1
    else:
        freq[s[i]]=1
        
        
sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

print(sorted_freq)