s = "abcbaa"
k = 3

substrings = set()  # to avoid duplicates
l = len(s)

for i in range(l):
    st = set()
    for j in range(i, l):
        st.add(s[j])
        if len(st) == k:
            substrings.add(s[i:j+1])
        elif len(st) > k:
            break

print(len(substrings))
