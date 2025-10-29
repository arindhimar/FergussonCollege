cardScore = [5, 4, 1, 8, 7, 1, 3 ]
k = 3

l = len(cardScore)
st = 0
et = l - 1
ct = 0
p = 0

while ct < k:
    if cardScore[st] > cardScore[et]:
        p += cardScore[st]
        st += 1
    else:
        p += cardScore[et]
        et -= 1
    ct += 1

print(p)
