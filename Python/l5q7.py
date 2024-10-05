f = open("aurEknew.txt","r")
text = f.read()

word_counts = {}

for word in text.split():
    word = word.lower()  
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

# myValue = list(word_counts.values())
# myValue.sort(reverse=True)
word_counts1  = {key:val for key,val in sorted(word_counts.items(),key=lambda x:-x[1])}

print(word_counts1)