s = "aabcbaa"
l = len(s)
total_beauty = 0

for i in range(l):
    freq = {}
    for j in range(i, l):
        ch = s[j]
        freq[ch] = freq.get(ch, 0) + 1
        
        if len(freq) > 1:  
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            total_beauty += max_freq - min_freq

print("Sum of Beauty of all substrings:", total_beauty)
