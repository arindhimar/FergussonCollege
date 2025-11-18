a= [0.1, 0.5, 0.9]
b = [0.2, 0.4, 0.8]


aUb=[max(x,y) for x,y in zip(a,b)]

aIb=[min(x,y) for x,y in zip(a,b)]

aC=[1-x for x in a]

aCb1=[((x+y)-(x*y)) for x,y in a,b]

aCb12=[(x*y) for x,y in a,b]



