f = open("random.txt","r")
 
# print(f.read().split(" "))

word_count={}

for temp in f.read().split(" "):
    if temp in word_count:
        word_count[temp]+=1
    else:
        word_count[temp] = 1
        

print(sorted(word_count.items(),key = lambda x:x[1],reverse=True))        

# print(word_count)