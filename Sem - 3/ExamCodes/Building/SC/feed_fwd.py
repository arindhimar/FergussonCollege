def feed_forward(x1, x2, x3, x4):
    s = x1*w1 + x2*w2 + x3*w3 + x4*w4
    return s

def bipolar_step_function(x):
    return 1 if x >= 0 else -1

def neural_network(x1, x2, x3, x4):
    out1 = feed_forward(x1, x2, x3, x4)
    out2 = feed_forward(x1, x2, x3, x4)
    
    out3 = out1 * w5 + out2 * w6
    out4 = out1 * w7 + out2 * w8
    
    final_input = out3 + out4
    final_output = bipolar_step_function(final_input)
    
    return final_output

w1,w2,w3,w4 = 0.1,0.2,0.3,0.4
w5,w6,w7,w8 = 0.5,0.6,0.7,0.8

print(neural_network(1, -1, 0, 0))
