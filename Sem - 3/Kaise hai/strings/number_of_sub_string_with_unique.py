s = "pqpqs"
k = 2  
count = 0
l = len(s)

for i in range(l):
    st = set()
    for j in range(i, l):
        st.add(s[j])
        if len(st) >= k:
            count += 1
        

print(count)
