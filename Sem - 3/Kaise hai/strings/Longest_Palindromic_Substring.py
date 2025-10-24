s = "babad"
l = len(s)
max_pal = ""
max_len = 0

for i in range(l):
    for j in range(i+1, l+1):
        sub = s[i:j]
        
        if sub == sub[::-1] and len(sub) > max_len:
            max_pal = sub
            max_len = len(sub)

print("Longest palindromic substring:", max_pal)
print("Length:", max_len)
