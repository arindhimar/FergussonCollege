a= [0.1, 0.5, 0.9]
b = [0.2, 0.4, 0.8]

aUb=[max(x,y) for x,y in zip(a,b)]
aUbC=[(1-x) for x in aUb]

# print(aUb)

aC= [(1-x) for x in a]
bC= [(1-x) for x in b]

# print(aC)
# print(bC)

aCIbC=[min(x,y) for x,y in zip(aC,bC)]

# print(aCIbC)

print(aUbC==aCIbC)



