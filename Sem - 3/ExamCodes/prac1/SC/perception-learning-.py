X = [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]

Y = [0, 1, 1, 1]

weights = [0.0, 0.0]
bias = 0.0
learning_rate = 0.1

def activation_fn(net):
    return 1 if net > 0 else 0

for epoch in range(10):
    for i in range(len(X)):
        net = X[i][0]*weights[0] + X[i][1]*weights[1] + bias
        output = activation_fn(net)
        error = Y[i] - output

        
        weights[0] += learning_rate * X[i][0]
        weights[1] += learning_rate * X[i][1]
        bias += learning_rate * error


print("Final weights:", weights)
print("Final bias:", bias)
