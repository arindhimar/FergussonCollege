a=[0.5,0.6]

b=[0.2,0.4]

#c1=a+b
c1=[a[0]+b[0],a[1]+b[1]]

#c2=a-b
c2=[a[0]-b[1],a[1]-b[0]]

#c3=a*b
p=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
c3=(min(p),max(p))

#c4=a/b
q=(a[0]/b[0],a[0]/b[1],a[1]/b[0],a[1]/b[1])
c4=(min(q),max(q))

print("a+b=",c1)
print("a-b=",c2)
print("a*b=",c3)
print("a/b=",c4)


