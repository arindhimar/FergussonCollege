s = "0214638"

tempS = [int(ch) for ch in s]

l=len(tempS)

i=l-1

while i>=0:
    if tempS[i]%2!=0:
        break

    i=i-1

print(s[0:i+1])