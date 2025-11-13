import math

x1, x2 = 0.5, 0.3
w1, w2 = 0.4, 0.7
b = 0.2


net = (x1*w1)+(x2*w2)+b

binary=1/(1-math.exp(-net))
bipolar=1-math.exp(-net)/(1+math.exp(-net))