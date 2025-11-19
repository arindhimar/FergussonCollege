def f(net):
    if net>=1:
        return 1
    else: 
        return 0

w1=w2=w3=w4=w5=w6=w7=w8=0.2

i1=i2=0.4

h11=i1*w1+i2*w3
h22=i1*w2+i2*w4


h1=f(h11)
h2=f(h22)


c11=h1*w5+h2*w7
c22=h1*w6+h2*w8

print(c11,c22)

c1=f(c11)
c2=f(c22)

print(c1,c2)


