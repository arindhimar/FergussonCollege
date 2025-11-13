a=[0.1,0.6,0.5,0.9]
b=[0.2,0.4,0.8,0.3]


#union
aUb=[max(x,y) for x,y in zip(a,b)]
print(aUb)


#intersection
aIb=[min(x,y) for x,y in zip(a,b)]
print(aIb)

#complement
aC=[(1-x) for x in a]
bC=[(1-y) for y in b]

print(aC)
print(bC)
