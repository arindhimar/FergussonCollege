s = "abcba"
ct = 0
l = len(s)

for i in range(l):
    st = set()
    for j in range(i, l):
        st.add(s[j])
        if len(st) == 3:
            ct += 1

print(ct)
