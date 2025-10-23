words = ["flower", "flow", "flight"]

minL = min(len(word) for word in words)

str=""

for i in range(minL):
    ch=words[0][i]
    
    for j in range(len(words)):
        if words[j][i]!=ch:
            break
    
    str+=ch
    
    
print(str)