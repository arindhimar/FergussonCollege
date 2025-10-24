symbols = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

ls = len(symbols)

s = "MCMXCIV"

l=len(s)

num=0

for i in range(l):
    if i<l-1 and symbols[s[i]]<symbols[s[i+1]]:
        num-=symbols[s[i]]
    else:
        num+=symbols[s[i]]
        

print(num)
    