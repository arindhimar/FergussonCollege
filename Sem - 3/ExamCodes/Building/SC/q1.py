#sample fuzzy set 
# take len
a= [0.1, 0.5, 0.9]
b = [0.2, 0.4, 0.8]



#union of both
unionAB=[max(x,y) for x,y in zip(a,b)]
print(unionAB)

#intersection
intersectionAB=[min(x,y) for x,y in zip(a,b)]
print(intersectionAB)

#complement
cA=[(1-x) for x in a]
cB=[(1-y) for y in b]
print(cA)
print(cB)

#algebric sum
algebricSum=[ ((x+y)-(x*y)) for x,y in zip(a,b)]
print(algebricSum)

#algebric product
algebricProduct=[(x*y) for x,y in zip(a,b)]
print(algebricProduct)

#cartesian producy
l=3
cp=[]
for i in range(3):
    tcp=[]
    for j in range(3):
        tcp.append(min(a[i],b[j]))
    
    cp.append(tcp)
    
print(cp)